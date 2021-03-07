import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
#from prediction import *
from brain_scan import prediction

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Specify the place to store the uploaded images
UPLOAD_FOLDER = 'static/uploads/'

# Create the flask app
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# Set the requirement for valid upload files
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Create the route for homepage upload.html
@app.route('/')
def upload_form():
    return render_template('upload.html')


# Take User uploaded images and perform prediction
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pred = prediction.prediction(filename)
        flash('The prediction is ' + pred)
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


# Create the route for the page after the prediction is made
# and show the images uploaded
@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    size = 10
    return redirect(url_for('static',
                    filename='uploads/' + filename, code=301))


# Create the route for Data description page data.html
@app.route('/data', methods=['GET', 'POST'])
def data_page():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('upload_form'))

    # show the form, it wasn't submitted
    return render_template('data.html')


# Create the route for the model page about.html
@app.route('/about', methods=['GET', 'POST'])
def about_page():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('upload_form'))
    return render_template('about.html')


# Create the route for the future endeavours page future.html
@app.route('/future', methods=['GET', 'POST'])
def future_page():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('upload_form'))
    return render_template('future.html')


# Create the route for about the team page team.html
@app.route('/team', methods=['GET', 'POST'])
def team_page():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('upload_form'))
    return render_template('team.html')


if __name__ == "__main__":
    app.run()

'''
Citing the references sources of code:
https://roytuts.com/upload-and-display-image-using-python-flask/
'''
