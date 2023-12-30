import requests
from seleniumbase import BaseCase
from utils.helper import assert_list_text


class TestShopPage(BaseCase):

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

    def test_verify_categories_text(self):
        self.open("https://practice-react.sdetunicorns.com/shop-grid-standard")

        # Expected texts for each li item
        expected_texts = ["All Categories", "Laptop", "Electronics", "Keyboard"]

        # Verify the text of each li item
        assert_list_text(self, ".sidebar-widget-list.mt-30 li", expected_texts)
        # for i, text in enumerate(expected_texts, start=1):
        #     self.assert_text(text, f'.sidebar-widget-list.mt-30 li:nth-child({i})')
