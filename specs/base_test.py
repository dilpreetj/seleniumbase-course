from seleniumbase import BaseCase
import requests
import os
from config.default import BROWSERSTACK_BASE_URL


class BaseTest(BaseCase):
    def update_bs_status(self, status):
        session_id = self.driver.session_id
        bs_username = os.environ.get("BROWSERSTACK_USERNAME")
        bs_access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")
        auth_credentials = (bs_username, bs_access_key)
        url = f"{BROWSERSTACK_BASE_URL}/automate/sessions/{session_id}.json"
        payload = {"status": status}
        requests.put(url, auth=auth_credentials, json=payload)

    def tearDown(self):
        status = "failed" if self._outcome.errors else "passed"
        self.update_bs_status(status)
        super().tearDown()
