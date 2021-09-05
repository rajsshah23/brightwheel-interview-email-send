from fastapi import APIRouter, Depends

from app.models.get_email_status_models import (
    GetEmailStatusResponse,
    GetEmailStatusRequest,
)
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)
from app.route_helpers.send_email_helper import SendEmailHelper

send_email_router: APIRouter = APIRouter()


@send_email_router.post("/email/send", response_model=SendEmailResponse)
def send_email(
    request: SendEmailRequest, helper: SendEmailHelper = Depends(SendEmailHelper)
) -> SendEmailResponse:
    return helper.send_email(request=request)


@send_email_router.get("/email/{id}/status", response_model=GetEmailStatusResponse)
def get_email_status(id: str, helper: SendEmailHelper = Depends(SendEmailHelper)):
    return helper.get_email_status(request=GetEmailStatusRequest(email_send_id=id))
