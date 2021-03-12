import unittest
from brain_scan import app

class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_about_page_get(self):
        rv = self.app.get('/future')
        self.assertTrue('<!-- Future Endeavors -->' in str(rv.data)) #successful load of about page

    def test_about_page_post(self):
        rv = self.app.post('/about')
        self.assertTrue('302 FOUND' == str(rv.status))
