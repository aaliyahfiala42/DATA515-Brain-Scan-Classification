import unittest
from brain_scan import model


class TestModelPreProcessFile(unittest.TestCase):
    def test_pre_process_file(self):
        my_model = model.Model()
        directory = 'tests/mock_data'
        filename = 'no.jpg'

        im, label = my_model._Model__pre_process_file(directory, filename)

        self.assertTrue(len(im) == 240)
        self.assertTrue(label == 0)
