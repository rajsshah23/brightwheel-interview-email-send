from fastapi import Depends

from app.clients.email_send_client import EmailSendClient
from app.clients.snailgun_client import SnailgunClient
from app.clients.spendgrid_client import SpendgridClient
from app.dependencies import get_settings
from app.models.email_send_vendor import EmailSendVendor
from app.setup.settings import Settings


def make_email_send_client(
    settings: Settings = Depends(get_settings)
) -> EmailSendClient:
    if settings.EMAIL_SEND_VENDOR == EmailSendVendor.spendgrid:
        return SpendgridClient(settings=settings)
    elif settings.EMAIL_SEND_VENDOR == EmailSendVendor.snailgun:
        return SnailgunClient(settings=settings)
    else:
        raise NotImplemented()
