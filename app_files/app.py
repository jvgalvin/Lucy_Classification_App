from flask import Flask

UPLOAD_FOLDER = '/Users/johngalvin/Desktop/GitHub/Tensorflow/workspace/Lucy-Classification/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER