import unittest
from brain_scan import app


class TestDataPage(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_data_page_get(self):
        rv = self.app.get('/data')
        self.assertTrue('<!-- Data Description -->' in str(rv.data))

    def test_data_page_post(self):
        rv = self.app.post('/data')
        self.assertTrue('302 FOUND' == str(rv.status))
