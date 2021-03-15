import unittest
from brain_scan import model


class TestModelPredictFromPath(unittest.TestCase):
    def test_model_predict_from_path_no_network(self):
        # Checks error handling if model has not been loaded
        my_model = model.Model()
        self.assertRaises(NotImplementedError, my_model.predict_from_path, '')

    def test_model_predict_from_path_yes_network(self):
        # Checks error handling if model has been loaded
        my_model = model.Model()
        x, y = my_model.load_data(['tests/mock_data'])
        my_model.train(x, y, num_epochs=1)

        # Even though prediction is incorrect for yes image
        # We can use the consistent incorrect prediction for testing
        prediction = my_model.predict_from_path('/tests/mock_data/yes.jpg')
        self.assertTrue(prediction == "No")
