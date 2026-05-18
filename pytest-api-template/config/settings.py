import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "http://localhost")
    PORT = os.getenv("PORT", "8080")
    FULL_BASE_URL = f"{BASE_URL}:{PORT}"
    
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "password123")
    
    TIMEOUT = 10

settings = Settings()
