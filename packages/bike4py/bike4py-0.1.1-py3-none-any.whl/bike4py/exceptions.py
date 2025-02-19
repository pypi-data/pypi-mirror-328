class LLMClientError(Exception):
    """Base exception for LLM client"""
    pass

class AuthenticationError(LLMClientError):
    """Raised when authentication fails"""
    pass

class APIError(LLMClientError):
    """Raised when API returns an error"""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}") 