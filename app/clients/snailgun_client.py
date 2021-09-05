from logging import Logger
from typing import Dict

import requests
from fastapi import Depends
from requests import Response
from structlog import get_logger

from app.clients.email_send_client import EmailSendClient
from app.dependencies import get_settings
from app.exceptions import SnailgunSendException, SnailgunSendNon200Response
from app.models.send_email_models import SendEmailRequest, SendEmailResponse
from app.models.snailgun_models import (
    SnailgunSendEmailRequest,
    SnailgunSendEmailResponse,
)
from app.setup.settings import Settings


logger: Logger = get_logger()


class SnailgunClient(EmailSendClient):
    def __init__(self, settings: Settings = Depends(get_settings)):
        super(SnailgunClient, self).__init__(settings=settings)

    def send_email(self, request: SendEmailRequest) -> SendEmailResponse:
        try:
            url: str = self._settings.SNAILGUN_BASE_URL
            headers: Dict[str, str] = {
                "Content-Type": "application/json",
                "X-Api-Key": self._settings.SNAILGUN_API_KEY,
            }

            body: SnailgunSendEmailRequest = SnailgunSendEmailRequest(
                from_email=request.from_email,
                from_name=request.from_name,
                to_email=request.to,
                to_name=request.to_name,
                subject=request.subject,
                body=request.body,
            )

            response: Response = requests.post(
                url=url, headers=headers, json=request.dict()
            )
            logger.info("Snailgun email send response", response_text=response.text)

            if response.status_code != 200:
                logger.error(
                    "Received a non-200 OK HTTP response status from Snailgun",
                    received_status=response.status_code,
                    response_text=response.text,
                    request=request.dict(),
                    url=url,
                    body=body.dict(),
                )
                raise SnailgunSendNon200Response()
            parsed_response: SnailgunSendEmailResponse = SnailgunSendEmailResponse(
                **response.json()
            )

            return SendEmailResponse(
                request=request, send_status=parsed_response.status
            )
        except Exception as e:
            logger.error(
                "Encountered an error while attempting to send an email via Snailgun.",
                request=request.dict(),
                exc_info=e,
            )
            raise SnailgunSendException from e
