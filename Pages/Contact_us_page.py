from pathlib import Path


class ContactUsPage:
    def __init__(self, page):
        self.page = page

        # Navigation
        self.contact_us_link = page.locator("a[href='/contact_us']")

        # Form Elements
        self.name_input = page.locator("input[name='name']")
        self.email_input = page.locator("input[name='email']")
        self.subject_input = page.locator("input[name='subject']")
        self.message_textarea = page.locator("textarea#message")
        self.upload_file_input = page.locator("input[name='upload_file']")
        self.success_message = page.locator('.status.alert.alert-success')


        # Submit
        self.submit_button = page.locator("input[type='submit']")

        # Success confirmation
        self.success_text = page.locator("text=Success! Your details have been submitted successfully.")

        # Home / Navigation after submit
        self.home_button = page.locator("a:has-text('Home')")





    def upload_file(self):
        file_path = Path.cwd() / "testdata" / "sample.txt"
        self.upload_file_input.set_input_files(str(file_path))
        files = self.upload_file_input.evaluate("el => el.files[0].name")
        assert files == "sample.txt"

    def handle_pop_up(self):
        self.page.on('dialog',lambda dialog:dialog.accept())
