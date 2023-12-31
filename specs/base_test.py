from seleniumbase import BaseCase
import requests


class BaseTest(BaseCase):
    def update_bs_status(self, status):
        session_id = self.driver.session_id
        auth_credentials = ('dilpreetj_tsvpl4', 'CtEEf6v5zYySKBpdR4w6')
        url = f"https://api.browserstack.com/automate/sessions/{session_id}.json"
        payload = {"status": status}
        requests.put(url, auth=auth_credentials, json=payload)

    def tearDown(self):
        status = "failed" if self._outcome.errors else "passed"
        self.update_bs_status(status)
        super().tearDown()