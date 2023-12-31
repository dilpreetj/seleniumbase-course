import pytest
from seleniumbase import BaseCase
from pages.upload_page import UploadPage
from utils.helper import get_image_path
from specs.base_test import BaseTest


class TestUploadPage(BaseTest):
    @pytest.mark.smoke
    def test_upload_single_file(self):
        upload_page = UploadPage(self)

        upload_page.open()

        # provide the file path
        file_path = get_image_path("sb_logo.png")

        upload_page.upload_single_file(file_path)

        # assert file uploaded
        self.assert_text("Image uploaded successfully", upload_page.success_message)

    @pytest.mark.smoke
    @pytest.mark.long_running_test
    def test_upload_multiple_files(self):
        upload_page = UploadPage(self)

        upload_page.open()

        # provide the file path
        file_path_1 = get_image_path("sb_logo.png")
        file_path_2 = get_image_path("Selenium_Logo.png")

        upload_page.upload_multiple_files([file_path_1, file_path_2])

        # assert file uploaded
        self.assert_text("Images uploaded successfully", upload_page.success_message)
