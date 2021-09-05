from logging import Logger
from typing import Dict

import requests
from fastapi import Depends
from requests import Response

from app.clients.email_send_client import EmailSendClient
from app.dependencies import get_settings
from app.exceptions import SpendgridSendException, SpendgridSendNon200Response
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)
from app.models.spendgrid_models import SpendgridSendEmailRequest
from app.setup.settings import Settings
from structlog import get_logger

logger: Logger = get_logger()


class SpendgridClient(EmailSendClient):
    def __init__(self, settings: Settings = Depends(get_settings)):
        super(SpendgridClient, self).__init__(settings=settings)

    def send_email(self, request: SendEmailRequest) -> SendEmailResponse:
        try:
            url: str = f"{self._settings.SPENDGRID_BASE_URL}/send_email"
            headers: Dict[str, str] = {
                "Content-Type": "application/json",
                "X-Api-Key": self._settings.SPENDGRID_API_KEY,
            }

            body: SpendgridSendEmailRequest = SpendgridSendEmailRequest(
                sender=f"{request.from_name} {request.from_email}",
                recipient=f"{request.to_name} {request.to}",
                subject=request.subject,
                body=request.body,
            )

            response: Response = requests.post(
                url=url, headers=headers, data=body.dict()
            )
            logger.info("Spendgrid email send response", response_text=response.text)

            if response.status_code != 200:
                logger.error(
                    "Received a non-200 OK HTTP response status from Spendgrid",
                    received_status=response.status_code,
                    response_text=response.text,
                    request=request.dict(),
                    url=url,
                    body=body.dict(),
                )
                raise SpendgridSendNon200Response()

            return SendEmailResponse(request=request, send_status=EmailSendStatus.sent)
        except Exception as e:
            logger.error(
                "Encountered an error while attempting to send an email via Spendgrid.",
                request=request.dict(),
                exc_info=e,
            )
            raise SpendgridSendException from e
