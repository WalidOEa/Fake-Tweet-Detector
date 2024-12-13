from flask import Flask, request, jsonify
import joblib
import numpy as np

import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Heroku!"

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))  # Default to 5000 if $PORT is not set
   app.run(debug=False, host='0.0.0.0', port=port)