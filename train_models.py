import pandas as pd
import numpy as np
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import os

# Function to clean text
def clean_text(text):
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove special characters, numbers, and punctuation
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

def main():
    print("Loading emotion dataset...")
    # Load the dataset
    data_path = "./data/emotion_dataset_raw.csv"
    df = pd.read_csv(data_path)
    
    # Print dataset info
    print(f"Dataset shape: {df.shape}")
    print(f"Emotions in the dataset: {df['Emotion'].unique()}")
    print(f"Number of samples per emotion: \n{df['Emotion'].value_counts()}")
    
    # Clean the text data
    print("Cleaning text data...")
    df['Clean_Text'] = df['Text'].apply(clean_text)
    
    # Create feature and target variables
    X = df['Clean_Text']
    y = df['Emotion']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    # Create a pipeline with TF-IDF and Logistic Regression
    print("Creating and training the model pipeline...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
        ('clf', LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000, random_state=42))
    ])
    
    # Train the model
    pipeline.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    print("Saving the model...")
    # Create models directory if it doesn't exist
    os.makedirs("./models", exist_ok=True)
    model_path = "./models/emotion_classifier_pipe_lr.pkl"
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()