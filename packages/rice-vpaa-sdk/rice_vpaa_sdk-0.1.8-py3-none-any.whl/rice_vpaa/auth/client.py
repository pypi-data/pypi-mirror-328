from typing import Optional
import requests
from .models import AuthToken, AuthUser
from ..config import BASE_URL

class AuthClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.token: Optional[str] = None
    
    def login(self, username: str, password: str) -> bool:
        """Login and get access token"""
        response = self.session.post(
            f"{self.base_url}/auth/token",
            data={
                "username": username,
                "password": password
            }
        )
        
        if response.status_code == 200:
            token = AuthToken.model_validate(response.json())
            self.token = token.access_token
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
            return True
        return False
    
    def get_current_user(self) -> Optional[AuthUser]:
        """Get current authenticated user"""
        if not self.token:
            return None
            
        response = self.session.get(f"{self.base_url}/auth/me")
        
        if response.status_code == 200:
            return AuthUser.model_validate(response.json())
        return None
    
    def logout(self):
        """Clear authentication token"""
        self.token = None
        self.session.headers.pop("Authorization", None) 