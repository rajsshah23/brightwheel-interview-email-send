from fastapi import APIRouter, Depends
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)
from app.route_helpers.send_email_helper import SendEmailHelper

send_email_router: APIRouter = APIRouter()


@send_email_router.post("/", response_model=SendEmailResponse)
def send_email(
    request: SendEmailRequest, helper: SendEmailHelper = Depends(SendEmailHelper)
) -> SendEmailResponse:
    return helper.send_email(request=request)
