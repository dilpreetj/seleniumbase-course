from seleniumbase import BaseCase


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # assert url and title contains SDET Unicorns
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDET Unicorns')

    def test_search_flow(self):
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click('.search-active')

        # type Lenovo in the search input field
        self.type("[placeholder='Search']", 'Lenovo')

        # click on search button
        self.click('.button-search')

        # assert the text is visible
        self.assert_text_visible('Showing Results for Lenovo')

    def test_search_flow_with_xpath(self):
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click("//button[@class='search-active']")

        # type Lenovo in the search input field
        self.type("//input[@placeholder='Search']", 'Lenovo')

        # click on search button
        self.click("//button[@class='button-search']")

        # assert the text is visible
        self.assert_text_visible('Showing Results for Lenovo')
