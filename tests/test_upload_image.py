import unittest
import sys
# sys.path.append('../brain_scan/')
# import main
from brain_scan import application

class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()
        
    def test_upload_image_get(self):
        rv = self.app.get('/upload')
        self.assertTrue('<!-- Home Page/Upload picture for prediction -->' in str(rv.data))
        
    def test_upload_image_post(self):
        rv = self.app.post('/upload')
        self.assertTrue('302 FOUND' == str(rv.data))
        
    def test_upload_image_file_not_in_request(self):
        results = application.upload_image()
        
        self.assertEquals(results, redirect(request.url))
    
    def test_upload_image_empty_filename(self):
        results = application.upload_image()
        
        self.assertEquals(results, redirect(request.url))
        
    def test_allowed_image_upload(self):
        results = application.upload_image()
        
        self.assertEquals(results, render_template('upload.html', filename=filename))
        
    def test_not_allowed_image_upload(self):
        results = application.upload_image()
        
        self.assertEquals(results, redirect(request.url))
