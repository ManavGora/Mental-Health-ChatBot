# app/models/classifier.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib
from app.utils.data_loader import load_data

def train_classifier(data_path: "data/dataset.csv"):
    """
    Train a text classification model using TF-IDF vectorizer and logistic regression.

    Parameters:
    - data_path (str): Path to the dataset CSV file.

    Returns:
    None
    """
    # Load the dataset
    data, labels = load_data(data_path)
    
    # Create a pipeline with a TF-IDF vectorizer and a logistic regression classifier
    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(data, labels)
    
    # Save the trained model
    joblib.dump(model, "app/models/classifier.pkl")

if __name__ == "__main__":
    train_classifier("data/dataset.csv")
