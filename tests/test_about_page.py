import unittest
from brain_scan import app


class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_about_page_get(self):
        rv = self.app.get('/about')
        # Look for unique header in loaded html
        self.assertTrue('<!-- Model Information -->' in str(rv.data))

    def test_about_page_post(self):
        rv = self.app.post('/about')
        self.assertTrue('302 FOUND' == str(rv.status))
