from unittest import TestCase

import requests
from mockito import mock, unstub, expect
from requests import Response

from app.clients.spendgrid_client import SpendgridClient
from app.models.send_email_models import (
    SendEmailRequest,
    SendEmailResponse,
    EmailSendStatus,
)


class TestSnailgunClient(TestCase):
    def setUp(self) -> None:
        super(TestSnailgunClient, self).setUp()

    def tearDown(self) -> None:
        super(TestSnailgunClient, self).tearDown()

        unstub()

    # TODO: Add tests for the following cases:
    #  1. Happy path
    #  2. When server returns non-200
