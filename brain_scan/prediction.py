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


# Take the uploaded images and perform 
# prediction (model is loaded as a .h5 file)
def prediction(path):
    model = tf.keras.models.load_model(str(root) + '/brain_scan/final_model.h5')
    image = cv2.imread(str(root) + "/brain_scan/static/uploads/" + path)
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
