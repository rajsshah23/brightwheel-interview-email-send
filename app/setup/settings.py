from pydantic import BaseSettings

from app.models.email_send_vendor import EmailSendVendor


class Settings(BaseSettings):
    APP_NAME: str = "brightwheel-interview-email-send"

    EMAIL_SEND_VENDOR: EmailSendVendor

    SPENDGRID_API_KEY: str
    SNAILGRID_API_KEY: str

    class Config:
        env_file = ".env"
