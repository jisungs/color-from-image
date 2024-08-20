from flask import Flask, render_template, redirect, url_for, request
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(['index.html'])





if __name__ == '__main__':
    app.run(debug=True, port=5002)