import unittest
from brain_scan import model

class TestModelInit(unittest.TestCase):
    def test_init_args_given(self):
        my_model = model.Model('/brain_scan/final_model.h5', 123123)
        self.assertTrue(my_model.network) # Check that the h5 was loaded 


    def test_init_no_args(self):
        # This test also covers cases where only one arg is given
        my_model = model.Model()
        self.assertFalse(my_model.network) # Check network set to None

