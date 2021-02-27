from flask import Flask

# Specify the place to store the uploaded images
UPLOAD_FOLDER = 'static/uploads/'

# Create the flask app
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024