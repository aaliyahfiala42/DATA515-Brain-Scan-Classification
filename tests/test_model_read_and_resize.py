import unittest
from brain_scan import model


class TestModelReadAndResize(unittest.TestCase):
    def test_model_read_and_resize(self):
        my_model = model.Model()

        image_size = my_model.IMAGE_SIZE  # Image size constant
        filepath = 'tests/mock_data/yes.jpg'

        resized_im = my_model._Model__read_and_resize(filepath)

        self.assertTrue(len(resized_im) == len(resized_im[0]) == image_size)
