import tensorflow as tf
import cv2
import numpy as np


# Take the uploaded images and perform prediction (model is loaded as a .h5 file)
def prediction(path):
    model = tf.keras.models.load_model('./final_model.h5')
    image = cv2.imread("./static/uploads/"+path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reshape the image so that it fits the model required input format
    image = cv2.resize(image, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    test_array = np.array(image)
    reshape_array = test_array.reshape(-1, 240, 240, 1)
    predictions = model.predict(reshape_array, batch_size=32)

    if predictions[0][0] == 1:
        return ('Yes')
    else:
        return ("No")