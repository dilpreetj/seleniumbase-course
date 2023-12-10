from seleniumbase import BaseCase


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # assert url and title contains SDET Unicorns
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDET Unicorns')
