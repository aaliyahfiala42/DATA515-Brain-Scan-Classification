import unittest
from brain_scan import model


class TestModelLoadData(unittest.TestCase):
    def test_load_data(self):
        my_model = model.Model()
        x, y = my_model.load_data(['tests/mock_data'])
        self.assertTrue(len(x[0]) == len(x[1]) == 240)
        self.assertTrue(len(y) == 2)
