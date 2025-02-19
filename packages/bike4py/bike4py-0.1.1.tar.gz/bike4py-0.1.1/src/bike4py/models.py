from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin
import aiohttp

DEFAULT_BASE_URL = "https://app.bike4mind.com"

class ServerConfig(BaseModel):
    """Server configuration returned by /api/settings/serverConfig"""
    apiUrl: str
    websocketUrl: str
    appfileBucketName: str
    fabfileBucketName: str
    pdfExpressViewerKey: str
    googleClientId: str

class ServiceURLs(BaseModel):
    """Service URL configuration"""
    base_url: str = Field(default=DEFAULT_BASE_URL)
    server_config: Optional[ServerConfig] = None

    @classmethod
    async def create(cls, base_url: str = DEFAULT_BASE_URL) -> 'ServiceURLs':
        """Factory method to create ServiceURLs with server config"""
        service_urls = cls(base_url=base_url)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(service_urls.server_config_url) as response:
                    if response.status == 200:
                        config_data = await response.json()
                        service_urls.server_config = ServerConfig(**config_data)
        except Exception:
            # If we can't fetch the config, we'll fall back to default behavior
            pass
        return service_urls

    @property
    def completion_url(self) -> str:
        return urljoin(self.base_url, "api/ai/llm")
    
    @property
    def websocket_url(self) -> str:
        if self.server_config:
            return self.server_config.websocketUrl
        # Fallback to default behavior if no server config
        return self.base_url.replace("http://", "ws://").replace("https://", "wss://")
    
    @property
    def auth_url(self) -> str:
        return urljoin(self.base_url, "api/auth/refreshToken")
    
    @property
    def server_config_url(self) -> str:
        return urljoin(self.base_url, "api/settings/serverConfig")

    @property
    def upload_url(self) -> str:
        return urljoin(self.base_url, "api/files/createFabFile")

class AuthTokens(BaseModel):
    access_token: str
    refresh_token: str

class ChatCompletionParameters(BaseModel):
    model: Optional[str] = None
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    max_tokens: Optional[int] = 1000
    presence_penalty: Optional[float] = 0.0
    frequency_penalty: Optional[float] = 0.0
    logit_bias: Optional[Dict[str, float]] = None
    stream: Optional[bool] = True

class ChatCompletionRequest(BaseModel):
    sessionId: str
    message: str
    params: ChatCompletionParameters
    historyCount: int = 0
    fabFileIds: List[str] = []

class KnowledgeType(str, Enum):
    URL = 'URL'
    FILE = 'FILE'
    TEXT = 'TEXT'

class FileUploadRequest(BaseModel):
    type: KnowledgeType = KnowledgeType.FILE
    fileName: str
    mimeType: str
    fileSize: int
    public: bool = False
    tags: List[Dict[str, float]] = []
