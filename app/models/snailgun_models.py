import datetime

from pydantic import EmailStr
from pydantic.main import BaseModel

# TODO: Add field descriptions
from app.models.send_email_models import EmailSendStatus


class SnailgunSendEmailRequest(BaseModel):
    from_email: EmailStr
    from_name: str
    to_email: EmailStr
    to_name: str
    subject: str
    body: str


class SnailgunSendEmailResponse(BaseModel):
    id: str
    from_email: EmailStr
    from_name: str
    to_email: EmailStr
    to_name: str
    subject: str
    body: str
    status: EmailSendStatus
    created_at: datetime.datetime
