import tensorflow as tf
import cv2
import numpy as np
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
# Remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass


class Image():
    """
    A class ued to represent an image (np array)
    ---------
    Attribute:
    path : str
        a string that is the path to where the image is located
    ---------
    Methods:
        read_from_path()
            read the image from the given path
        process()
            change the image to grayscale and resize the image
    """

    def __init__(self, path):
        """
        :param path: str
            the path to where the image is located
        """

        self.path = path

    def read_from_path(self):
        """
        Read in the image file from the path provided when object is created
        and return a numpy array of the image
        :return: <class 'numpy.ndarray'>
            the numpy array of the image
        """

        image = cv2.imread(str(root) + "/brain_scan/static/uploads/" + self.path)

        return image

    def process(self):
        """
        conver the image to grayscale and resize the image to be 240x240
        :return: <class 'numpy.ndarray'>
            the processed numpy array of the image with shape (1, 240, 240, 1)
        """

        image = cv2.cvtColor(self.read_from_path(), cv2.COLOR_BGR2GRAY)

        # Reshape the image so that it fits the model required input format
        image = cv2.resize(image, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
        test_array = np.array(image)
        reshape_array = test_array.reshape(-1, 240, 240, 1)


        return reshape_array

class Model():
    """
    A class ued to represent the tensorflow model
    ---------
    Attribute:
    path : str
        a string that is the path to where the model is located
    ---------
    Methods:
        read_from_path()
            load the model from the path that is given
        predict()
            use the loaded ts flower model to make a preidction on input python array
    """

    def __init__(self, path):
        self.path = path

    def read_from_path(self):
        """
        Load the tf model from the path provided when object is created
        :return: <class 'tensorflow.python.keras.engine.sequential.Sequential'>
        """

        model = tf.keras.models.load_model(str(root) + self.path)

        return model

    def prediction(self,array):
        """
        Perform a model prediction using the tf model on the input array

        :param array:
            a numpy array of the resized image with shape (1, 240, 240, 1)
        :return: str:
            A string of "Yes" or "No" depends on the prediction result
        """

        predictions = self.read_from_path().predict(array, batch_size=32)

        if predictions[0][0] == 1:
            return ('Yes')
        else:
            return ("No")


"""
Example Usage: 

image = Image("Y70.jpg")
model = Model("/brain_scan/final_model.h5")

print(model.prediction(image.process()))
"""