from seleniumbase import BaseCase


class TestAboutPage(BaseCase):
    def test_assert_equal(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        welcome_text = self.get_text('.welcome-content h5')
        self.assert_equal(welcome_text, 'Who Are We')

    def test_assert_true(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        is_breadcrumb_visible = self.is_element_visible('.breadcrumb-area')
        self.assert_true(is_breadcrumb_visible)

    def test_assert_element_visible(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_element_visible('.banner-area')

    def test_assert_element_present(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_element_present('#hidden-span')

    def test_assert_in(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        welcome_text = self.get_text('.welcome-content h1')
        self.assert_in('Welcome', welcome_text)

    def test_assert_attribute(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_attribute('.breadcrumb-content a', 'aria-current', 'page')

    def test_assert_false(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        hidden_span = self.is_element_visible('#hidden-span') # false

        self.assert_false(hidden_span)

    def test_assert_not_equal(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        header_offer = self.get_text('.header-offer span') # $200

        self.assert_not_equal(header_offer, '$0')

    def test_assert_element_not_visible(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_element_not_visible('#hidden-span')

    def test_assert_text_not_visible(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_text_not_visible('$0', '.header-offer span')

    def test_assert_attribute_not_present(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_attribute_not_present('.breadcrumb-content a', 'href', 'google.com')