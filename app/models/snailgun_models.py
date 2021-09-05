import datetime

from pydantic import EmailStr
from pydantic.main import BaseModel

from app.models.send_email_models import EmailSendStatus

# TODO: Add descriptions for the fields
class SnailgunSendEmailRequest(BaseModel):
    from_email: EmailStr
    from_name: str
    to_email: EmailStr
    to_name: str
    subject: str
    body: str


# TODO: Add descriptions for the fields
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
