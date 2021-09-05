from pydantic.main import BaseModel

from app.models.send_email_models import EmailSendStatus


class GetEmailStatusRequest(BaseModel):
    email_send_id: str


class GetEmailStatusResponse(BaseModel):
    email_send_id: str
    status: EmailSendStatus
