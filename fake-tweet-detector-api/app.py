from flask import Flask, request, jsonify
import joblib
import numpy as np

import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Heroku!"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')