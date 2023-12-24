from seleniumbase import  BaseCase
from config.default import BASE_URL


class HomePage:
    """
    Page object class for Home Page

    Encapsulates all interactions with the Home Page
    """
    def __init__(self, sb: BaseCase):
        self.sb = sb

        # locators
        self.search_input = '.search-active'
        self.search_placeholder = "[placeholder='Search']"
        self.search_button = '.button-search'
        self.product_link = '.main-menu  li:nth-child(2)'
        self.about_link = '.footer-list [href="/about"]'
        self.copyright_link = '.copyright p a'
        self.nav_links = '.main-menu  li'

    def open(self):
        self.sb.open(BASE_URL)

    def search_for_item(self, item):
        self.sb.click(self.search_input)
        self.sb.type(self.search_placeholder, item)
        self.sb.click(self.search_button)

    def verify_nav_links(self, expected_nav_text):
        """
        Verifies the text of nav links against expected text
        :param expected_nav_text: A list of expected text for each nav link
        """
        for i, text in enumerate(expected_nav_text, start=1):
            self.sb.assert_text(text, f'{self.nav_links}:nth-child({i})')
