import unittest
from io import BytesIO
from brain_scan import app


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['Testing'] = True
        self.client = self.app.test_client()
        
    def test_upload_image(self):
        res = self.client.post('/', data = dict(file = (io.BytesIO(b"This is a test"), 'test.jpeg'),), follow_redirects = True)
        assert res.status_code == 200
        assert 'file saved' in res.data
