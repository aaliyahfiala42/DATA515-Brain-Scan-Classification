import unittest
from io import BytesIO
from brain_scan import app


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['Testing'] = True
        self.client = self.app.test_client()

    def test_upload_image(self):
        data = dict(
                file=(BytesIO(b'This is a test'), "test.jpeg"),
                    )
        response = self.client.post('/', content_type='image/gif',
                                    data=data, follow_redirects=True)

        assert response.status_code == 200

    def test_upload_image_fail(self):

        response = self.client.post('/', content_type='image/gf',
                                    follow_redirects=True)

        assert b'No file part' in response.data
        
    '''
    def test_no_upload_image(self):
        data = dict(
            file=(BytesIO(b'This is a test'), '',)
                  )
        
        response = self.client.post('/', content_type = '',
                                    data=data, follow_redirects=True)
        
        assert b'No image selected for uploading' in response.data
    '''
    
    def test_upload_image_not_allowed(self):
        
        response = self.client.post('/', content_type='text/xml',
                                    follow_redirects=True)
        
        assert b'Allowed image types are -> png, jpg, jpeg' in response.data
