## Brain Scan Classification
### DATA 515 Final Project
Location: http://aaliyahhanni.pythonanywhere.com/

The Brain Scan Classification is a machine learning project that classifies 2D brain scan images as tumorous or not. Our website allows users to upload their own (.jpg) photos into the model, and get a prediciton result. 
![image](https://user-images.githubusercontent.com/73403238/109405348-9590a400-7924-11eb-8eec-64639a7b33a1.png)

### How It Works
1. Navigate to http://aaliyahhanni.pythonanywhere.com/
2. Click the 'Choose File' button, and select the 2D .jpg brain scan from your file explorer
3. Click the 'Submit' button, and wait for the results to display at the top of the page

### About the Model
For this project, we are using a 2D Convolution Neural Network with one hidden layer to classify 2D MRI brain scan images as tumorous our not. It is built with Tensorflow and Keras. The input images (data set is described in the "Data Description" tab) are 240x240x1 the 1 indicates 1 channel and converted into grayscale. The output is just a 1D array the length of the samples, for exmaple if input 100 images are inputed, the model would output 100 predictions of 1 or 0 for whether or not there is a tumor.

[Include Snippets of Code & More General Details]

Number of Epoch:
Learning Rate:
Accuracy:

<img src=https://user-images.githubusercontent.com/73403238/109405511-3338a300-7926-11eb-997e-a63ba93bf3b6.png width="300"/>

Our model is trained on a data set from Kaggel Brain MRI Images for Brain Tumor Detection. The data consist of 253 images among which 155 images are labeled "yes" and 98 images labeled "no". 

MRI Scan without a Tumor
<img src = "http://aaliyahhanni.pythonanywhere.com/static/img/no.jpeg" alt = "No_tumor" style = "width:300px;">

MRI Scan with a Tumor (notated with arrow)
<img src = "http://aaliyahhanni.pythonanywhere.com/static/img/yes.jpg" alt = "Yes_tumor" style = "width:300px;">


### Limitations
Our initial goal was to build a model that takes in 3D MRI images, that give a complete view of the Brain, but were unable to accomplish this due to limited access to processing power. An example of a 3D MRI scan is shown below. 
<br />
<img src=https://user-images.githubusercontent.com/73403238/109405543-78f56b80-7926-11eb-9e1a-4dd4ec1644d7.png  width="300"/>


### Authors 
Aaliyah Fiala, Jordan Fields, Vanessa Hsu, Trevor Nims, Alyson Suchodolski, Sabrina Wang
