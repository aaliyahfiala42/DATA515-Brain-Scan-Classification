import unittest
from brain_scan import app

class TestUploadForm(unittest.TestCase):
    def setUp(self):
        '''
        Flask testing is confusing, but I'm 99% sure it is necessary
        to init a test client to check for template rendering
        '''
        self.app = application.app.test_client()

    def test_upload_form(self):       
        '''
        Tests for successful rendering of template on '/' GET route
        '''
        rv = self.app.get('/') # Stores response from '/' GET route as data attribute`
        # HTML comment is a unique identifier in upload.html
        self.assertTrue('<!-- Home Page/Upload picture for prediction -->' in str(rv.data)) 
