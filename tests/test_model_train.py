import unittest
from brain_scan import model
from tensorflow import keras


class TestModelTrain(unittest.TestCase):
    def test_model_train(self):
        my_model = model.Model()
        x, y = my_model.load_data(['tests/mock_data'])
        my_model.train(x, y, num_epochs=1)  # Saves to /models

        loaded_model = keras.models.load_model('models/best_classifier.h5')

        self.assertTrue(my_model.network._network_nodes ==
                        loaded_model._network_nodes)
