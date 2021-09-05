from fastapi import APIRouter
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)

send_email_router: APIRouter = APIRouter()


@send_email_router.post("/", response_model=SendEmailResponse)
def send_email(request: SendEmailRequest) -> SendEmailResponse:
    return SendEmailResponse(request=request, send_status=EmailSendStatus.queued)
