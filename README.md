[![Build Status](https://travis-ci.com/aaliyahfiala42/DATA515-Brain-Scan-Classification.svg?branch=main)](https://travis-ci.com/aaliyahfiala42/DATA515-Brain-Scan-Classification) 

## Brain Scan Classification
### DATA 515 Final Project
Project Website Location: http://doihaveatumor.com/

The Brain Scan Classification is a machine learning project that classifies 2D brain scan images as tumorous or not. 
Our website allows users to upload their own (.jpg, jpeg, or .png) photos into the model, and get a prediction result. 
<img src="/brain_scan/static/img/home.PNG">

## How It Works
1. Navigate to the 'Do I Have A Tumor?' website: http://doihaveatumor.com/
2. Click the 'Choose File' button, and select a 2D .jpg / .jpeg / .png brain scan from your file explorer
3. Click the 'Submit' button, and wait for the results to display at the top of the page

## About the Model
For this project, we are using a 2D Convolutional Neural Network with nine hidden layers to classify 2D MRI brain scan 
images as tumorous or non-tumorous. Our model was built with Tensorflow, utilizing the Keras API. Our model's input 
(data set is described in the "Data Description" tab) is composed of standardized 240x240x1 single-channel image arrays. 
After training, an image passed to the model will produce a prediction of either 1 (tumorous) or 0 (non-tumorous).


Below is our model's architecture in python, as well as an illustration:
```
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
```

<img src=/brain_scan/static/img/nn.png>

Our model is trained on a data set from Kaggle Brain MRI Images for Brain Tumor Detection. The data consist of 253 
images among which 155 images are labeled "yes" and 98 images labeled "no".


Below are two sample images from the data set:

| MRI Scan without a Tumor  | MRI Scan with a Tumor (notated with arrow)|
| :---: | :---: |
| <img src = "/brain_scan/static/img/no.jpeg" alt = "No_tumor" width ="300" >  | <img src = "/brain_scan/static/img/yes.jpg" alt = "Yes_tumor" width = "280" >  |
## How to Train Our Model
If you'd like to fiddle with any of the inner-workings of our model, all code used in its 
creation can be found in the 'notebooks' directory under the filename 
'brain_tumor_classification_FINAL.ipynb'. To ensure that the notebook can identify the location
of the dataset, please specify its location in cell 4.

## How to Use the Model (from GitHub)
To use our model in your own code, use the following function:

```
import tensorflow as tf
import cv2
import numpy as np

def prediction(input_filepath):
    model = tf.keras.models.load_model(final_model.h5')
    image = cv2.imread(input_filepath)
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
```
## Limitations
Our initial goal was to build a model that trained on 3D MRI images and thus get a more complete view of the brain/possible tumors.
However, this type of volumetric input necessitated a 3D Convolutional Neural Network, which we were unable to train effectively
due to limited processing power and memory on our local machines. In the future, we hope to have access to the hardware
necessary to implement this type of model.

A gif of a all 155 slices of a 3D MRI scan is shown below:
<br />
<p align="center">
<img src=http://aaliyahhanni.pythonanywhere.com/static/img/MRI.gif  width="300"/>
</p>

## Authors 
Aaliyah Hänni, Jordan Fields, Vanessa Hsu, Trevor Nims, Alyson Suchodolski, Sabrina Wang
