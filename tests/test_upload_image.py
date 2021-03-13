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
                file=(BytesIO(b'This is a test'), "test.pickle"),
                    )
        response = self.client.post('/', content_type='image/gif',
                                    data=data, follow_redirects=True)

        assert response.status_code == 200
