import asyncio
import json
import os
from typing import AsyncIterator, Optional, Union, TypedDict
from enum import Enum
from dataclasses import dataclass
import httpx
import websockets
from .auth import TokenManager
from .models import ChatCompletionRequest, FileUploadRequest, ServiceURLs
from .exceptions import APIError

DEFAULT_BASE_URL = "https://app.bike4mind.com"

class EventType(Enum):
    STATUS = "status"
    CONTENT = "content"
    COMPLETION = "completion"

@dataclass
class StatusEvent:
    status: str
    details: Optional[str] = None
    event_type: EventType = EventType.STATUS

@dataclass
class ContentEvent:
    content: str
    event_type: EventType = EventType.CONTENT

@dataclass
class CompletionEvent:
    success: bool
    message: Optional[str] = None
    event_type: EventType = EventType.COMPLETION

Event = Union[StatusEvent, ContentEvent, CompletionEvent]

class LLMClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        refresh_token: Optional[str] = None
    ):
        self.base_url = base_url
        self.urls: Optional[ServiceURLs] = None
        self.token_manager: Optional[TokenManager] = None
        self._refresh_token = refresh_token
        self._websocket: Optional[websockets.WebSocketClientProtocol] = None

    async def connect(self) -> None:
        """Establish WebSocket connection"""
        if self._websocket:
            return

        # Initialize ServiceURLs if not already done
        if not self.urls:
            self.urls = await ServiceURLs.create(base_url=self.base_url if self.base_url else DEFAULT_BASE_URL)
            self.token_manager = TokenManager(self.urls.auth_url)

        access_token = await self.token_manager.get_access_token(self._refresh_token)
        self._websocket = await websockets.connect(
            self.urls.websocket_url + "?token=" + access_token
        )

    async def disconnect(self) -> None:
        """Close WebSocket connection"""
        if self._websocket:
            await self._websocket.close()
            self._websocket = None

    async def submit_prompt(self, request: ChatCompletionRequest) -> None:
        """Submit a prompt for processing"""
        if not self._websocket:
            raise RuntimeError("WebSocket connection not established. Call connect() first.")

        access_token = await self.token_manager.get_access_token()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.urls.completion_url,
                json=request.model_dump(),
                headers={"Authorization": f"Bearer {access_token}"}
            )
            
            if response.status_code != 200:
                raise APIError(response.status_code, response.text)

    def _parse_event(self, raw_event: dict) -> Event:
        """Parse raw event data into appropriate event type"""
        if raw_event.get("statusMessage", None) is not None:
            return StatusEvent(
                status=raw_event["statusMessage"],
                details=raw_event.get("details")
            )

        quest = raw_event.get("quest", None)
        if quest is None:
            return None

        reply = quest.get("replies", None)
        if reply is not None:
            reply = reply[0]
        else:
            reply = quest.get("reply", None)

        if reply is None:
            return None

        if quest.get("status", "running") == "done":
            return CompletionEvent(success=True, message=reply)
        else:
            return ContentEvent(content=reply)

    async def stream_events(self) -> AsyncIterator[Event]:
        """Stream typed events from the WebSocket connection"""
        if not self._websocket:
            raise RuntimeError("WebSocket connection not established. Call connect() first.")

        while True:
            try:
                message = await self._websocket.recv()
                raw_event = json.loads(message)
                parsed_event = self._parse_event(raw_event)
                if parsed_event is not None:
                    yield parsed_event
            except websockets.ConnectionClosed:
                break

    async def upload_file(self, file: str, mime_type: str) -> str:
        """Upload a file to the service"""
        async with httpx.AsyncClient() as client:
            upload_request = FileUploadRequest(
                fileName=file,
                mimeType=mime_type,
                fileSize=os.path.getsize(file),
            )
            access_token = await self.token_manager.get_access_token()
            create_response = await client.post(
                self.urls.upload_url,
                json=upload_request.model_dump(),
                headers={"Authorization": f"Bearer {access_token}"}
            )
            upload_response = await client.put(
                create_response.json()["presignedUrl"],
                files={"file": (file, open(file, "rb"), mime_type)},
                headers={"Content-Type": mime_type}
            )
            if upload_response.status_code != 200:
                raise APIError(upload_response.status_code, upload_response.text)
            return create_response.json()["_id"]

    async def __aenter__(self):
        """Context manager entry"""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        await self.disconnect() 