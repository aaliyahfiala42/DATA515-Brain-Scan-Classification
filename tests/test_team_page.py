import unittest
from brain_scan import app


class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_about_page_get(self):
        rv = self.app.get('/team')
        self.assertTrue('<!-- Team member information -->' in str(rv.data))

    def test_about_page_post(self):
        rv = self.app.post('/team')
        self.assertTrue('302 FOUND' == str(rv.status))
