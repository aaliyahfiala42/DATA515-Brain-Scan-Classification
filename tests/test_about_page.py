import unittest
import sys
sys.path.append('../brain_scan/')
import main

class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_about_page_get(self):
        rv = self.app.get('/about')
        self.assertTrue('<!-- Model Information -->' in str(rv.data)) #successful load of about page

    def test_about_page_post(self):
        rv = self.app.post('/about')
        self.assertTrue('302 FOUND' == str(rv.status))
