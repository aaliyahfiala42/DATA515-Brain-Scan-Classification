import unittest
from cStringIO import StringIO
from brain_scan import app


class TestUploadImage(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['Testing'] = True
        self.client = self.app.test_client()
        
    def test_upload_image(self):
        res = self.client.post('/', data = {upload_var = (StringIO('test'), 'test.txt'),})
        assert res.status_code == 200
        assert 'file saved' in res.data