from fastapi import Depends

from app.dependencies import get_settings
from app.models.get_email_status_models import (
    GetEmailStatusRequest,
    GetEmailStatusResponse,
)
from app.models.send_email_models import SendEmailRequest, SendEmailResponse
from app.setup.settings import Settings


class EmailSendClient:
    def __init__(self, settings: Settings = Depends(get_settings)):
        self._settings: Settings = settings

    def send_email(self, request: SendEmailRequest) -> SendEmailResponse:
        raise NotImplemented()

    def get_email_status(
        self, request: GetEmailStatusRequest
    ) -> GetEmailStatusResponse:
        raise NotImplemented()
