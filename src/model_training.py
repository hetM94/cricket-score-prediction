import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

from data_preprocessing import preprocess_data, load_data

def train_model(X, y):
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Save the trained model to a .pkl file
    model_filename = '../models/cricket_score_model.pkl'
    joblib.dump(model, model_filename)
    print(f"Model saved to {model_filename}")

    return model

if __name__ == "__main__":
    file_path = '../data/t20.csv'
    df = load_data(file_path)
    df = preprocess_data(df)

    # Define feature columns (X) and target column (y)
    feature_columns = ['runs', 'balls']  # Use balls for better prediction
    target_column = 'runs'

    X = df[feature_columns]
    y = df[target_column]

    # Train the model
    model = train_model(X, y)
