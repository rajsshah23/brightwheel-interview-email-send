from unittest import TestCase

from mockito import unstub, mock

from app.clients.email_send_client import EmailSendClient
from app.clients.snailgun_client import SnailgunClient
from app.clients.spendgrid_client import SpendgridClient
from app.clients.utils import make_email_send_client
from app.models.email_send_vendor import EmailSendVendor


class TestUtils(TestCase):
    def setUp(self) -> None:
        super(TestUtils, self).setUp()

    def tearDown(self) -> None:
        super(TestUtils, self).tearDown()

        unstub()

    def test_make_email_send_client_spendgrid(self):
        self._settings = mock()
        self._settings.EMAIL_SEND_VENDOR = EmailSendVendor.spendgrid

        actual: EmailSendClient = make_email_send_client(settings=self._settings)

        self.assertEqual(type(actual.__class__), type(SpendgridClient))

    def test_make_email_send_client_snailgun(self):
        self._settings = mock()
        self._settings.EMAIL_SEND_VENDOR = EmailSendVendor.snailgun

        actual: EmailSendClient = make_email_send_client(settings=self._settings)

        self.assertEqual(type(actual.__class__), type(SnailgunClient))
