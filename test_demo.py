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

    def test_dropdown(self):
        self.open("https://seleniumbase.io/demo_page")

        # before state
        self.assert_element('meter[value="0.25"]')

        self.select_option_by_index('#mySelect', '2')
        self.assert_element('meter[value="0.75"]')

        self.select_option_by_text('#mySelect', 'Set to 100%')
        self.assert_element('meter[value="1"]')

        self.select_option_by_value('#mySelect', '50%')
        self.assert_element('meter[value="0.5"]')

    def test_iframe(self):
        # root DOM
        self.open("https://seleniumbase.io/demo_page")
        self.assert_element_not_visible('h4')

        # switch frame to 2
        self.switch_to_frame('#myFrame2')
        self.assert_element('h4')
        self.assert_text('iFrame Text', 'h4')

        # root DOM
        self.switch_to_default_content()
        self.assert_element('#progressBar')

    def test_checkbox(self):
        self.open("https://seleniumbase.io/demo_page")

        # assert image logo is not visible
        self.assert_element_not_visible('img#logo')

        # assert checkbox is not selected
        self.assert_false(self.is_selected('#checkbox1'))

        # click on the checkbox
        self.click('#checkbox1')

        # assert checkbox is selected
        self.assert_true(self.is_selected('#checkbox1'))

        # assert image logo is now visible
        self.assert_element_visible('img#logo')

