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

        self.assertTrue(response.status_code == 200)

    def test_upload_image_fail(self):

        response = self.client.post('/', content_type='image/gif',
                                    follow_redirects=True)

        self.assertTrue(b'No file part' in response.data)

    def test_upload_image_good_file(self):
        im = open('tests/mock_data/yes.jpg', 'rb')
        response = self.client.post('/', data=im, follow_redirects=True)
        im.close()
        self.assertTrue('!-- Home Page/Upload picture for prediction -->'
                        in str(response.data))
