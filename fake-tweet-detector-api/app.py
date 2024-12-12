from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('knn_model.pkl')  # Load your trained KNN model
vectorizer = joblib.load('vectorizer.pkl')  # Load the vectorizer (e.g., TfidfVectorizer)

@app.route('/classify', methods=['POST'])
def classify_tweet():
    # Get tweet data from the incoming request
    data = request.json
    tweet = data.get('tweet', '')
    
    if not tweet:
        return jsonify({'error': 'No tweet provided'}), 400
    
    # Preprocess the tweet using the same method as during training
    processed_tweet = vectorizer.transform([tweet])  # Convert tweet to feature vector
    
    # Predict using the model
    prediction = model.predict(processed_tweet)
    
    # Classify as "Fake" or "Real"
    result = "Fake" if prediction[0] == 1 else "Real"
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)