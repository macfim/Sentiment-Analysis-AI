from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes to allow requests from your frontend

# Load Model
pipe_lr = joblib.load(open("./models/emotion_classifier_pipe_lr.pkl", "rb"))

# Function to predict emotions
def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

emotions_emoji_dict = {"anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗", "joy": "😂", "neutral": "😐", "sad": "😔", "sadness": "😔", "shame": "😳", "surprise": "😮"}

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Emotion Classifier API",
        "endpoints": {
            "/predict": "POST - Predict emotion from text",
            "/emotions": "GET - List all possible emotions"
        }
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text for analysis'}), 400
    
    text = data['text']
    
    prediction = predict_emotions(text)
    probability = get_prediction_proba(text)
    
    # Convert probability array to dict for JSON response
    proba_dict = {emotion: float(prob) for emotion, prob in zip(pipe_lr.classes_, probability[0])}
    
    response = {
        'text': text,
        'prediction': prediction,
        'confidence': float(np.max(probability)),
        'emoji': emotions_emoji_dict.get(prediction, ""),
        'probabilities': proba_dict
    }
    
    return jsonify(response)

@app.route('/emotions', methods=['GET'])
def list_emotions():
    return jsonify({
        'emotions': list(pipe_lr.classes_),
        'emotions_with_emoji': emotions_emoji_dict
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)