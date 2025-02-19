import httpx
import time
from typing import Optional
from .models import AuthTokens
from .exceptions import AuthenticationError

class TokenManager:
    def __init__(self, auth_url: str):
        self.auth_url = auth_url
        self._tokens: Optional[AuthTokens] = None

    async def get_access_token(self, refresh_token: Optional[str] = None) -> str:
        """Get a valid access token, refreshing if necessary"""
        if refresh_token:
            await self.refresh_tokens(refresh_token)
        
        if not self._tokens:
            raise AuthenticationError("No tokens available")

        return self._tokens.access_token

    async def refresh_tokens(self, refresh_token: str) -> None:
        """Refresh access token using refresh token"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.auth_url,
                    json={"token": refresh_token}
                )
                response.raise_for_status()
                json = response.json()
                self._tokens = AuthTokens(
                    access_token=json["accessToken"],
                    refresh_token=json["refreshToken"]
                )
            except httpx.HTTPError as e:
                raise AuthenticationError(f"Token refresh failed: {str(e)}") 