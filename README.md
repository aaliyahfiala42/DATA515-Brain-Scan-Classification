## Brain Scan Classification
### DATA 515 Final Project
Location: http://aaliyahhanni.pythonanywhere.com/

The Brain Scan Classification is a machine learning project that classifies 2D brain scan images as tumorous or not. Our website allows users to upload their own (.jpg) photos into the model, and get a prediciton result. 
![image](https://user-images.githubusercontent.com/73403238/109405348-9590a400-7924-11eb-8eec-64639a7b33a1.png)

## How It Works
1. Navigate to http://aaliyahhanni.pythonanywhere.com/
2. Click the 'Choose File' button, and select the 2D .jpg brain scan from your file explorer
3. Click the 'Submit' button, and wait for the results to display at the top of the page

## About the Model
For this project, we are using a 2D Convolution Neural Network with one hidden layer to classify 2D MRI brain scan images as tumorous our not. It is built with Tensorflow and Keras. The input images (data set is described in the "Data Description" tab) are 240x240x1 the 1 indicates 1 channel and converted into grayscale. The output is just a 1D array the length of the samples, for exmaple if input 100 images are inputed, the model would output 100 predictions of 1 or 0 for whether or not there is a tumor.

[Include Snippets of Code & More General Details]

Initial Learning Rate: 0.01 <br />
Number of Total Training Epochs: 100 <br />
Final Validation Set Accuracy: .902

<img src=/brain_scan/static/img/nn.png>

Our model is trained on a data set from Kaggel Brain MRI Images for Brain Tumor Detection. The data consist of 253 images among which 155 images are labeled "yes" and 98 images labeled "no". 
<br />
MRI Scan without a Tumor
<br />
<img src = "http://aaliyahhanni.pythonanywhere.com/static/img/no.jpeg" alt = "No_tumor" width="300"/>
<br />
MRI Scan with a Tumor (notated with arrow)
<br />
<img src = "http://aaliyahhanni.pythonanywhere.com/static/img/yes.jpg" alt = "Yes_tumor" width="300"/>
<br />

## How to Use the Model (from GitHub)
[need to add more details, step-by-step guide of how to install and run on local machine]
![Use Case](https://user-images.githubusercontent.com/73403238/109585563-98240280-7ab8-11eb-8469-6290c813da10.jpg)


## Limitations
Our initial goal was to build a model that takes in 3D MRI images, that give a complete view of the Brain, but were unable to accomplish this due to limited access to processing power. An example of a 3D MRI scan is shown below. 
<br />
<img src=http://aaliyahhanni.pythonanywhere.com/static/img/MRI.gif  width="300"/>

## Authors 
Aaliyah Fiala, Jordan Fields, Vanessa Hsu, Trevor Nims, Alyson Suchodolski, Sabrina Wang
