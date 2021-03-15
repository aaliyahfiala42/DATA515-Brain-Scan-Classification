import unittest
from brain_scan import model
import numpy as np

class TestModelScaleAndNormalize(unittest.TestCase):
    def test_scale_and_normalize(self):
        my_model = model.Model()

        im_array = np.array([[1, 3],[1,3]])
        im_array = my_model._Model__scale_and_normalize(im_array)
        expected_output = np.array([[0, 1],[0, 1]])

        self.assertTrue((im_array == expected_output).all())
