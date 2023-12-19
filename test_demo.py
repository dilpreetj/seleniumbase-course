from seleniumbase import BaseCase


class TestDemoPage(BaseCase):
    def test_input_slider_control(self):
        self.open("https://seleniumbase.io/demo_page")

        # before state
        self.assert_attribute('#progressBar', 'value', '50')

        # change the slider value
        self.set_value('#mySlider', '80')

        # after state
        self.assert_attribute('#progressBar', 'value', '80')

