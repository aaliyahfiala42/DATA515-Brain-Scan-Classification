import unittest
import sys
# sys.path.append('../brain_scan/')
# import main
from brain_scan import application

class TestDisplayImage(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_display_image(self):
        rv = self.app.get('/display/no.jpeg')
        self.assertTrue(str(rv.status) == '302 FOUND') #function returns a successful redirect
