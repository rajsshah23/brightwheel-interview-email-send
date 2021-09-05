from pydantic import BaseSettings, HttpUrl

from app.models.email_send_vendor import EmailSendVendor


class Settings(BaseSettings):
    APP_NAME: str = "brightwheel-interview-email-send"

    EMAIL_SEND_VENDOR: EmailSendVendor

    SPENDGRID_API_KEY: str
    SNAILGUN_API_KEY: str
    SNAILGUN_BASE_URL: HttpUrl

    SPENDGRID_BASE_URL: HttpUrl

    class Config:
        env_file = ".env"
