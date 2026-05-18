import pytest
from api.teacher_client import TeacherClient
from config.settings import settings

class TestAuth:
    def test_login_success(self):
        client = TeacherClient()
        payload = {
            "username": settings.ADMIN_USERNAME,
            "password": settings.ADMIN_PASSWORD
        }
        response = client.login(payload)
        
        assert response.status_code == 200
        assert "authToken" in response.json()

    def test_login_invalid_credentials(self):
        client = TeacherClient()
        payload = {
            "username": "invalid_user",
            "password": "invalid_password"
        }
        response = client.login(payload)
        
        assert response.status_code == 401
        assert "error" in response.json()

    def test_access_without_token(self):
        client = TeacherClient() # No token
        response = client.get_all_teachers()
        
        assert response.status_code == 401
