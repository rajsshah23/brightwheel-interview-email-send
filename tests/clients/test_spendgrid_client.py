import json
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


class TestSpendgidClient(TestCase):
    def setUp(self) -> None:
        super(TestSpendgidClient, self).setUp()

        self._settings = mock()
        self._settings.SPENDGRID_BASE_URL = "https://google.com"
        self._settings.SPENDGRID_API_KEY = "foo"

        self._spendgrid_client: SpendgridClient = SpendgridClient(
            settings=self._settings
        )

    def tearDown(self) -> None:
        super(TestSpendgidClient, self).tearDown()

        unstub()

    def test_send_email_happy_path(self):
        # Setup
        self._request: SendEmailRequest = SendEmailRequest(
            **{
                "to": "rajsshah23@gmail.com",
                "to_name": "Raj Shah",
                "from": "noreply@mybrightwheel.com",
                "from_name": "brightwheel",
                "subject": "Your Weekly Report",
                "body": "<h1>Weekly Report</h1><p>You saved 10 hours this week!</p>",
            }
        )

        # Mock calls
        response: Response = Response()
        response.status_code = 200
        response._content = json.dumps(
            {
                "success": True,
                "id": "foo_email_id",
                "sender": "brightwheel <noreply@mybrightwheel.com>",
                "recipient": "Raj Shah <rajsshah23@gmail.com>",
                "subject": "Your Weekly Report",
                "body": "<h1>Weekly Report</h1><p>You saved 10 hours this week!</p>",
            }
        ).encode("utf-8")
        expect(times=1, obj=requests).post(
            url=f"{self._settings.SPENDGRID_BASE_URL}/send_email",
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": self._settings.SPENDGRID_API_KEY,
            },
            data=json.dumps(
                {
                    "sender": "brightwheel <noreply@mybrightwheel.com>",
                    "recipient": "Raj Shah <rajsshah23@gmail.com>",
                    "subject": "Your Weekly Report",
                    "body": "<h1>Weekly Report</h1><p>You saved 10 hours this week!</p>",
                }
            ),
        ).thenReturn(response)

        # Test
        expected: SendEmailResponse = SendEmailResponse(
            id="foo_email_id", request=self._request, send_status=EmailSendStatus.sent
        )

        actual: SendEmailResponse = self._spendgrid_client.send_email(
            request=self._request
        )

        self.assertEqual(expected, actual)

    # TODO: Add tests for the case when server returns non-200
