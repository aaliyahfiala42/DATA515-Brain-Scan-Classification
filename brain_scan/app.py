from brain_scan import model
import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
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

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Specify the place to store the uploaded images
UPLOAD_FOLDER = str(root) + '/brain_scan/static/uploads/'

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

        # Create the object Model imported from model.py with attribute of
        # the path to the saved model
        # use the predict_from_path function to perform the prediction
        # on uploaded image
        cnn_model = model.Model("/brain_scan/final_model.h5")
        pred = cnn_model.predict_from_path("/brain_scan/static/uploads/"
                                           + filename)

        flash('The prediction is ' + pred)
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)


# Create the route for the page after the prediction is made
# and show the images uploaded
@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
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
