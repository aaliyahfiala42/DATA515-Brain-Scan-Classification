import unittest
from brain_scan import app


class TestDisplayImage(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_display_image(self):
        rv = self.app.get('/display/no.jpeg')
        self.assertTrue(str(rv.status) == '302 FOUND')
