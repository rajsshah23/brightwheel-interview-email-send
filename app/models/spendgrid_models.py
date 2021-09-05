from pydantic.main import BaseModel

# TODO: Add field descriptions
class SpendgridSendEmailRequest(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str


class SpendgridSendEmailResponse(BaseModel):
    id: str
    sender: str
    recipient: str
    subject: str
    body: str
