import os.path

from seleniumbase import BaseCase
from pages.upload_page import UploadPage


class TestUploadPage(BaseCase):
    def test_upload_single_file(self):
        upload_page = UploadPage(self)

        upload_page.open()

        # provide the file path
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'sb_logo.png')
        )

        upload_page.upload_single_file(file_path)

        # assert file uploaded
        self.assert_text("Image uploaded successfully", upload_page.success_message)

    def test_upload_multiple_files(self):
        upload_page = UploadPage(self)

        upload_page.open()

        # provide the file path
        file_path_1 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'sb_logo.png')
        )
        file_path_2 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'Selenium_Logo.png')
        )

        upload_page.upload_multiple_files([file_path_1, file_path_2])

        # assert file uploaded
        self.assert_text("Images uploaded successfully", upload_page.success_message)
