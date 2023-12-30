from seleniumbase import BaseCase
from parameterized import parameterized


class TestContactForm(BaseCase):
    @parameterized.expand(
        [
            (
                "Roronoa Zoro",
                "zoro@onepiece.com",
                "Seeking Strong Swords",
                "become the world's greatest swordsman",
            ),
            (
                "Monkey D. Luffy",
                "luffy@onepiece.com",
                "Pirate King",
                "I'm gonna be the Pirate King!",
            ),
            (
                "Nami",
                "nami@onepiece.com",
                "Navigation Charts",
                "Looking for detailed navigation charts of the Grand Line.",
            ),
        ]
    )
    def test_form_submission_param(self, name, email, subject, message):
        self.open("https://practice-react.sdetunicorns.com/contact")

        # fill in the form fields
        self.type("input[name='name']", name)
        self.type("input[name='email']", email)
        self.type("input[name='subject']", subject)
        self.type("textarea[name='message']", message)

        # submit the form
        self.click("button[type='submit']")

        # Assertions
        self.assert_text(
            "Message sent successfully", ".react-toast-notifications__toast__content"
        )
        self.assert_element_not_visible("[class*=error]")

    def test_form_submission(self):
        self.open("https://practice-react.sdetunicorns.com/contact")

        # fill in the form fields
        self.type("input[name='name']", "Roronoa Zoro")
        self.type("input[name='email']", "zoro@onepiece.com")
        self.type("input[name='subject']", "Seeking Strong Swords")
        self.type(
            "textarea[name='message']",
            "I need details on rare and strong swords for my journey "
            "to become the world's greatest swordsman.",
        )

        # submit the form
        self.click("button[type='submit']")

        # Assertions
        self.assert_text(
            "Message sent successfully", ".react-toast-notifications__toast__content"
        )
        self.assert_element_not_visible("[class*=error]")

    def test_form_submission_without_input(self):
        self.open("https://practice-react.sdetunicorns.com/contact")

        # submit the form
        self.click("button[type='submit']")

        # assert the count of error messages
        errors_el = self.find_elements("[class*=error]")
        self.assert_true(len(errors_el) == 4)

        # assert the name field text error
        self.assert_text("Name is required", ".error-name")

        # Email is optional text should not be visible
        self.assert_false(self.is_text_visible("Email is optional", ".error-email"))

        # Subject error should be visible
        self.assert_element_visible(".error-subject")

        # Assert "Message" should be present in the error message
        error_message = self.get_text(".error-message")
        self.assert_in("Message", error_message)
