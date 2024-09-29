import joblib
import numpy as np

def predict_score(current_runs, current_overs):
    # Load the trained model
    model_filename = '../models/cricket_score_model.pkl'
    model = joblib.load(model_filename)

    # Convert overs to total balls
    current_balls = int(current_overs) * 6 + round((current_overs - int(current_overs)) * 6)

    # Prepare input features (runs and balls)
    X_input = np.array([[current_runs, current_balls]])

    # Make the prediction
    predicted_runs = model.predict(X_input)

    # Adjust prediction to reflect full match score
    total_overs = 20  # Assuming it's a T20 match
    balls_remaining = (total_overs * 6) - current_balls
    estimated_total_runs = predicted_runs[0] + (balls_remaining * (current_runs / current_balls))  # Estimation based on current scoring rate

    return estimated_total_runs

if __name__ == "__main__":
    current_runs = float(input("Enter current runs: "))
    current_overs = float(input("Enter current overs: "))

    predicted_score = predict_score(current_runs, current_overs)
    print(f"Predicted total runs: {predicted_score:.2f}")
