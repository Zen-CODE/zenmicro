from flask import Flask
from os import listdir

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/list')
def list_folder():
    contents = str(listdir("/app/Music"))
    return f'Hello Music! {contents}'
