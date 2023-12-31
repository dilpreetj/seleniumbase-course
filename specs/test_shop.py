from utils.helper import assert_list_text
from specs.base_test import BaseTest


class TestShopPage(BaseTest):
    def test_verify_categories_text(self):
        self.open("https://practice-react.sdetunicorns.com/shop-grid-standard")

        # Expected texts for each li item
        expected_texts = ["All Categories", "Laptop", "Electronics", "Keyboard"]

        # Verify the text of each li item
        assert_list_text(self, ".sidebar-widget-list.mt-30 li", expected_texts)
        # for i, text in enumerate(expected_texts, start=1):
        #     self.assert_text(text, f'.sidebar-widget-list.mt-30 li:nth-child({i})')
