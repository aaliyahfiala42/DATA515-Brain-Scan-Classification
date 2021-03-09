import unittest
import sys
# sys.path.append('../brain_scan/')
# import main
from brain_scan import application

class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()

    def test_about_page_get(self):
        rv = self.app.get('/team')
        self.assertTrue('<!-- Team member information -->' in str(rv.data)) #successful load of about page

    def test_about_page_post(self):
        rv = self.app.post('/team')
        self.assertTrue('302 FOUND' == str(rv.status))
