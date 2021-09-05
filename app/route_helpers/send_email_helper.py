from fastapi import Depends

from app.dependencies import get_settings
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)
from app.setup.settings import Settings


class SendEmailHelper:
    def __init__(self, settings: Settings = Depends(get_settings)):
        self._settings: Settings = settings

    def send_email(self, request: SendEmailRequest) -> SendEmailResponse:
        return SendEmailResponse(request=request, send_status=EmailSendStatus.queued)
