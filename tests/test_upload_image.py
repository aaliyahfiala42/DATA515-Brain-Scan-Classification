import unittest
from brain_scan import app


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['Testing'] = True
        self.client = self.app.test_client()

    def test_upload_image_success(self):
        with open('tests/mock_data/no.jpg', 'rb') as data:
            response = self.client.post('/',
                                        content_type='multipart/form-data',
                                        data={'file': data},
                                        follow_redirects=True)
            self.assertTrue('The prediction is'
                            in str(response.data))

    def test_upload_image_fail(self):

        response = self.client.post('/', content_type='image/gf',
                                    follow_redirects=True)

        assert b'No file part' in response.data
        
    def test_upload_image_incorrect_type(self):

        response = self.client.post('/', content_type='text/html',
                                    follow_redirects=True)

        assert b'Allowed image types are -> png, jpg, jpeg' in response.data
