import unittest
from brain_scan import app


class TestUploadForm(unittest.TestCase):
    def setUp(self):
        '''
        Flask testing is confusing, but I'm 99% sure it is necessary
        to init a test client to check for template rendering
        '''
        self.app = app.app.test_client()

    def test_upload_form(self):
        '''
        Tests for successful rendering of template on '/' GET route
        '''
        rv = self.app.get('/')
        self.assertTrue('<!-- Home Page/Upload picture for prediction -->'
                        in str(rv.data))
