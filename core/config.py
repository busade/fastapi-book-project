import secrets,os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage2"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 DEVOPS x BACKEND (Stage 2)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    EC2_PUBLIC_IP: str=os.getenv("EC2_PUBLIC_IP","ec2-13-61-190-61.eu-north-1.compute.amazonaws.com")
    THICK_URL: str = f"http://{EC2_PUBLIC_IP}/telex-webhook"
    SLACK_WEBHOOK_URL: str = os.getenv("TARGET_URL","")


settings = Settings()
