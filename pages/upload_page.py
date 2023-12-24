from seleniumbase import BaseCase
from config.default import BASE_URL


class UploadPage:
    def __init__(self, sb: BaseCase):
        self.sb = sb

        # Locators
        self.single_file_input = '.single input[type="file"]'
        self.multiple_file_input = '.multiple input[type="file"]'
        self.preview_image = '.preview img'
        self.upload_button = '.cart-main-area button'
        self.success_message = '.react-toast-notifications__toast__content'

    def open(self):
        self.sb.open(f"{BASE_URL}/upload")

    def _upload_file(self, file_selector, file_path):
        self.sb.choose_file(file_selector, file_path)
        self.sb.assert_element(self.preview_image)
        self.sb.click(self.upload_button)

    def upload_single_file(self, file_path):
        self._upload_file(self.single_file_input, file_path)

    def upload_multiple_files(self, file_paths):
        multiple_file_paths = '\n'.join(file_paths)
        self._upload_file(self.multiple_file_input, multiple_file_paths)
