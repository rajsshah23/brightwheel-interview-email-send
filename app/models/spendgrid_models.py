from pydantic.main import BaseModel

# TODO: Add field descriptions
class SpendgridSendEmailRequest(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str
