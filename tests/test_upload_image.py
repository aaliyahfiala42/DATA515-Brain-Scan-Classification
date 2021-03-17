import unittest
from io import BytesIO
from brain_scan import app


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['Testing'] = True
        self.client = self.app.test_client()

    def test_upload_image_success(self):
        '''
        This test is supposed to pass a file and verify that a prediction
        was given. Seems file name is not correctly passed to the client
        So we are unable to hit the if statement in upload_image
        that checks for the existence of file and that it has a 
        valid name.
        '''

        with open('tests/mock_data/no.jpg', 'rb') as data:
            response = self.client.post('/', content_type='multipart/form-data',
                                        data={'file': data}, follow_redirects=True)
            self.assertTrue('The prediction is'
                            in str(response.data))