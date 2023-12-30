from seleniumbase import BaseCase
from pages.home_page import HomePage
import pytest


class TestHomePage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp()  # call the setup of the parent class if needed
        self.homepage = HomePage(self)
        self.homepage.open()

        print('Login')

    def tearDown(self):
        print('Log Out')
        super().tearDown()

    @pytest.mark.smoke
    def test_verify_page_title_and_url(self):
        # assert url and title contains SDET Unicorns
        self.assert_url_contains("sdetunicorns")
        self.assert_title_contains("SDET Unicorns")

        print('TEST')

    @pytest.mark.search
    @pytest.mark.smoke
    def test_search_flow(self):
        self.homepage.search_for_item("Lenovo")

        # assert the text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    def test_search_flow_with_xpath(self):
        # click on the search input field
        self.click("//button[@class='search-active']")

        # type Lenovo in the search input field
        self.type("//input[@placeholder='Search']", "Lenovo")

        # click on search button
        self.click("//button[@class='button-search']")

        # assert the text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    def test_nav_links(self):

        self.assert_text("Products", self.homepage.product_link)

        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload"]

        self.homepage.verify_nav_links(expected_nav_text)

    def test_click_about_link_and_verify_url(self):
        # Click the "About" link
        self.click(self.homepage.about_link)

        # Assert URL
        self.assert_url_contains("about")

    def test_new_tab(self):
        self.click(self.homepage.copyright_link)

        self.switch_to_tab(1)

        self.assert_title_contains("Master Software Testing and Automation")

        self.switch_to_default_tab()

        self.assert_title_contains("Practice with React")
