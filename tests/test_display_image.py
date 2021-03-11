import unittest
from brain_scan import app

class TestDisplayImage(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()

    def test_display_image(self):
        rv = self.app.get('/display/no.jpeg')
        self.assertTrue(str(rv.status) == '302 FOUND') #function returns a successful redirect
