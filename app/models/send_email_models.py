import enum

from pydantic import BaseModel, EmailStr, Field


class EmailSendStatus(str, enum.Enum):
    queued = "queued"
    sent = "sent"
    failed = "failed"


class SendEmailRequest(BaseModel):
    to: EmailStr = Field(description="Email address to send the email to")
    to_name: str = Field(description="The name to accompany the email")
    from_email: EmailStr = Field(
        description="The email address in the from and reply fields", alias="from"
    )
    from_name: str = Field(description="the name to accompany the from/reply emails")
    subject: str = Field(description="The subject line of the email")
    body: str = Field(description="The HTML body of the email")


# TODO: Add descriptions for the fields
class SendEmailResponse(BaseModel):
    request: SendEmailRequest
    id: str
    send_status: EmailSendStatus
