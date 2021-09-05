from fastapi import Depends

from app.clients.email_send_client import EmailSendClient
from app.clients.utils import make_email_send_client
from app.dependencies import get_settings
from app.models.get_email_status_models import (
    GetEmailStatusRequest,
    GetEmailStatusResponse,
)
from app.models.send_email_models import SendEmailRequest, SendEmailResponse
from app.setup.settings import Settings


class SendEmailHelper:
    def __init__(
        self,
        settings: Settings = Depends(get_settings),
        email_send_client: EmailSendClient = Depends(make_email_send_client),
    ):
        self._settings: Settings = settings
        self._email_send_client: EmailSendClient = email_send_client

    def send_email(self, request: SendEmailRequest) -> SendEmailResponse:
        return self._email_send_client.send_email(request=request)

    def get_email_status(
        self, request: GetEmailStatusRequest
    ) -> GetEmailStatusResponse:
        return self._email_send_client.get_email_status(request=request)
