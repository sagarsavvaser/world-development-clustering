import joblib
import pandas as pd

# Load models
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca_model.pkl")
model = joblib.load("kmeans_model.pkl")

# Feature order used during training
FEATURE_COLUMNS = [
    "GDP",
    "Life Expectancy Female",
    "Life Expectancy Male",
    "Infant Mortality Rate",
    "Internet Usage",
    "Birth Rate",
    "Health Exp % GDP"
]

def predict_cluster(data):

    # Ensure correct column order
    data = data[FEATURE_COLUMNS]

    # Scale features
    scaled = scaler.transform(data)

    # Apply PCA
    pca_data = pca.transform(scaled)

    # Predict cluster
    cluster = model.predict(pca_data)

    return cluster[0]