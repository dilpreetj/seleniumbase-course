import os.path

from seleniumbase import BaseCase


class TestUploadPage(BaseCase):
    def test_upload_single_file(self):
        self.open("https://practice-react.sdetunicorns.com/upload")

        # provide the file path
        file_path = os.path.abspath('data/sb_logo.png')

        # file input selector
        file_input = '.single input[type="file"]'

        # upload file
        self.choose_file(file_input, file_path)

        # assert the file is visible
        self.assert_element('.preview img')

        # click the upload button
        self.click('.cart-main-area button')

        # assert file uploaded
        self.assert_text('Image uploaded successfully', ".react-toast-notifications__toast__content")

