from seleniumbase import BaseCase
from pages.home_page import HomePage


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        homepage = HomePage(self)

        # open home page
        homepage.open()

        # assert url and title contains SDET Unicorns
        self.assert_url_contains("sdetunicorns")
        self.assert_title_contains("SDET Unicorns")

    def test_search_flow(self):
        homepage = HomePage(self)

        homepage.open()

        homepage.search_for_item("Lenovo")

        # assert the text is visible
        self.assert_text_visible("Showing Results for Apple")

    def test_search_flow_with_xpath(self):
        self.open("https://practice-react.sdetunicorns.com/")

        # click on the search input field
        self.click("//button[@class='search-active']")

        # type Lenovo in the search input field
        self.type("//input[@placeholder='Search']", "Lenovo")

        # click on search button
        self.click("//button[@class='button-search']")

        # assert the text is visible
        self.assert_text_visible("Showing Results for Lenovo")

    def test_nav_links(self):
        homepage = HomePage(self)
        homepage.open()

        self.assert_text("Products", homepage.product_link)

        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload"]

        homepage.verify_nav_links(expected_nav_text)

    def test_click_about_link_and_verify_url(self):
        homepage = HomePage(self)
        homepage.open()

        # Click the "About" link
        self.click(homepage.about_link)

        # Assert URL
        self.assert_url_contains("about")

    def test_new_tab(self):
        homepage = HomePage(self)
        homepage.open()

        self.click(homepage.copyright_link)

        self.switch_to_tab(1)

        self.assert_title_contains("Master Software Testing and Automation")

        self.switch_to_default_tab()

        self.assert_title_contains("Practice with React")
