import unittest
from brain_scan import prediction

class TestPrediction(unittest.TestCase):
    def test_prediction_no_image(self):
        pred = prediction.prediction('no.jpeg')
        self.assertEqual(pred,('No'))

    def test_prediction_yes_image(self):
        pred = prediction.prediction('yes.jpg')
        self.assertEqual(pred,('Yes'))
