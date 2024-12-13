from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
model = joblib.load('fake-tweet-detector-api/knn_model.pkl')
vectorizer = joblib.load('fake-tweet-detector-api/vectorizer.pkl')

@app.route('/classify', methods=['POST'])
def classify_tweet():
    data = request.get_json()
    tweet = data.get('tweet', '')
    
    if not tweet:
        return jsonify({'error': 'No tweet provided'}), 400
    
    processed_tweet = vectorizer.transform([tweet])
    prediction = model.predict(processed_tweet)
    result = "Fake" if prediction[0] == 1 else "Real"
    
    return jsonify({'prediction': result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)