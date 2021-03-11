import unittest
from brain_scan import app

class TestDataPage(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()

    def test_data_page_get(self):
        rv = self.app.get('/data')
        self.assertTrue('<!-- Data Description -->' in str(rv.data)) #successful load of data description page

    def test_data_page_post(self):
        rv = self.app.post('/data')
        self.assertTrue('302 FOUND' == str(rv.status)) #sucessful redirect code

