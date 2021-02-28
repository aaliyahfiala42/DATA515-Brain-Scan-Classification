import tensorflow as tf
from keras.preprocessing import image
import numpy as np


# Take the uploaded images and perform prediction
# (model is loaded as a .h5 file)
def prediction(path):
    model = tf.keras.models.load_model('my_model.h5')
    test_img = image.load_img(
                "static\\uploads\\" + path, target_size=(150, 150))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    images = np.vstack([test_img])
    classes = model.predict(images, batch_size=10)
    if classes[0][0] == 1:
        return ('Yes')
    else:
        return ("No")
