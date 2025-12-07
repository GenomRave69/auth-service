import os

class Settings:
    PROJECT_NAME: str = "FastAPI Auth"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-default-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    SERVER_HOST: str = os.getenv("SERVER_HOST", "http://localhost:8000")
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:3000",]

settings = Settings()
