import numpy as np
from numpy.random import seed
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from datetime import datetime
import cv2
from os import listdir
import sys
from sklearn.utils import shuffle
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
# Remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass


class Model:
    """
    A class .....
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

    IMAGE_SIZE = 240

    def __init__(self, model_path=None, rand_seed=None):
        """
        Initializes the model, allows for the user to specify the random seed of the model for
        reproducibility.

        :param model_path: optional parameter, filepath to existing .h5 model to be used

        :param rand_seed: optional parameter, sets the seed for random number generation in
        both numpy and tensorflow to rand_seed
        """
        if model_path is not None:
            self.network = keras.models.load_model(str(root) + model_path)
        else:
            self.network = None

        if rand_seed is not None:
            seed(rand_seed)
            tf.random.set_seed(rand_seed)

    def load_data(self, directory_list):
        """
        Loads data from each directory in directory list, converting each image into a single channel
        positive globally standardized image array of shape (240, 240). Returns shuffled image arrays and labels.

        :param directory_list: List of directories which contain image data, each directory must be the parent
        of a group of image files with a path name ending in either 'yes' or 'no'

        :return X: A numpy array containing all transformed images, each with shape (IMAGE_SIZE, IMAGE_SIZE)
        :return y: A numpy array containing labels for each image, sharing indices with X
        """
        X = []
        y = []
        for directory in directory_list:
            for filename in listdir(directory):
                image, label = self.__pre_process_file(directory, filename)
                image = self.__scale_and_normalize(image)
                X.append(image)
                y.append(label)
        X = np.array(X)
        y = np.array(y)
        X, y = shuffle(X, y)
        return X, y

    def train(self, X, y, num_epochs=10):
        """
        Builds, compiles, and trains the neural network, saving tensorboard logs as well as the best model in the
        working directory.

        :param X: A numpy array of image arrays
        :param y: A numpy array of labels for each image, sharing indices with X
        :param num_epochs: optional parameter, number of epochs to train over
        """
        X = np.expand_dims(X, axis=3)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, shuffle=True, stratify=y)
        datagen = keras.preprocessing.image.ImageDataGenerator(rotation_range=30,
                                                               horizontal_flip=True,
                                                               vertical_flip=True,
                                                               validation_split=.2)
        model = keras.models.Sequential([
            keras.Input(shape=(240, 240, 1)),
            keras.layers.Conv2D(32, 3, strides=(1, 1), activation='relu', data_format='channels_last', name='conv0'),
            keras.layers.MaxPool2D((2, 2), name='max_pool0'),
            keras.layers.BatchNormalization(name='bn0'),
            keras.layers.Conv2D(64, 3, strides=(1, 1), activation='relu', data_format='channels_last', name='conv1'),
            keras.layers.MaxPool2D((2, 2), name='max_pool1'),
            keras.layers.BatchNormalization(name='bn1'),
            keras.layers.Conv2D(128, 3, strides=(1, 1), activation='relu', data_format='channels_last', name='conv2'),
            keras.layers.MaxPool2D((2, 2), name='max_pool2'),
            keras.layers.Flatten(),
            keras.layers.Dense(1, activation='sigmoid')])

        opt = keras.optimizers.Adam(learning_rate=0.01)
        model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['binary_accuracy'])

        logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
        model_path = 'models/best_classifier.h5'

        tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)

        # Save best model according to its validation set binary accuracy
        model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=model_path,
            monitor='val_binary_accuracy',
            mode='max',
            save_best_only=True)

        # Fit model using ImageDataGenerator on training data, unaltered testing data
        neural_net = model.fit(datagen.flow(X_train, y_train, batch_size=32),
                               epochs=num_epochs, shuffle=True,
                               validation_data=(X_test, y_test),
                               callbacks=[tensorboard_callback, model_checkpoint_callback])

        self.network = keras.models.load_model('models/best_classifier.h5')

    def predict_from_path(self, filepath):
        """
        After training the model or loading in one that was already made, this function will run the image
        contained at filepath through our model and output a prediction as a string.

        :param filepath: Filepath to image for prediction
        :return: Prediction of image containing a tumor as a string
        """
        image = cv2.imread(str(root) + filepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, dsize=(self.IMAGE_SIZE, self.IMAGE_SIZE), interpolation=cv2.INTER_CUBIC)
        test_array = np.array(image).astype('float32')
        test_array = self.__scale_and_normalize(test_array)
        test_array = np.expand_dims(test_array, axis=0)
        test_array = np.expand_dims(test_array, axis=3)
        predictions = self.network.predict(test_array, batch_size=32)

        if predictions[0][0] == 1:
            return 'Yes'
        return 'No'

    def __pre_process_file(self, directory, filename):
        """
        Load each image located at 'filename' with opencv, convert each image to grayscale and
        resize it to be of shape (IMAGE_SIZE, IMAGE_SIZE). Return the resized image and its label as an int.

        :param directory: directory where image file is located
        :param filename: Name of the image file

        :return image: Single channel grayscale image array of shape (IMAGE_SIZE, IMAGE_SIZE)
        :return label: Binary value with 1 indicting 'yes' and 0 indicating 'no'
        """
        image = cv2.imread(directory + '/' + filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, dsize=(self.IMAGE_SIZE, self.IMAGE_SIZE), interpolation=cv2.INTER_CUBIC)
        if directory[-3:] == 'yes':
            return image, 1
        # else directory[-3] == 'no'
        return image, 0

    def __scale_and_normalize(self, image_array):
        """
        Perform Positive Global Standardization on input array and return it.

        :param image_array: 2-dimensional image array containing int or float values

        :return arr: positive globally standardized arr of float values
        """
        arr = image_array.astype('float32')
        mean, stand_dev = arr.mean(), arr.std()
        arr = (arr - mean) / stand_dev
        arr = np.clip(arr, -1, 1)
        arr = (arr + 1) / 2
        return arr


"""
Example for prediction: 

model = Model("/brain_scan/final_model.h5")
print(model.predict_from_path("/brain_scan/static/uploads/Y54.JPG"))
"""
