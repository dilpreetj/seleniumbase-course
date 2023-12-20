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

    def test_upload_multiple_files(self):
        self.open("https://practice-react.sdetunicorns.com/upload")

        # provide the file path
        file_path_1 = os.path.abspath('data/sb_logo.png')
        file_path_2 = os.path.abspath('data/Selenium_Logo.png')

        # combine file paths into one
        multiple_file_paths = f'{file_path_1}\n{file_path_2}'

        # file input selector
        file_input = '.multiple input[type="file"]'

        # upload file
        self.choose_file(file_input, multiple_file_paths)

        # assert the file is visible
        self.assert_element('.preview img')

        # click the upload button
        self.click('.cart-main-area button')

        # assert file uploaded
        self.assert_text('Images uploaded successfully', ".react-toast-notifications__toast__content")
