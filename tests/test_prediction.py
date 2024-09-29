import unittest
import joblib
import os
import numpy as np
from src.prediction import predict_score


class TestPrediction(unittest.TestCase):

    def setUp(self):
        # Load model if exists
        self.model_filename = '../models/cricket_score_model.pkl'
        if not os.path.exists(self.model_filename):
            raise FileNotFoundError(f"Model file {self.model_filename} does not exist. Please train the model first.")
        self.model = joblib.load(self.model_filename)

    def test_predict_score(self):
        current_runs = 100
        current_overs = 10.0
        predicted_score = predict_score(current_runs, current_overs)
        self.assertIsInstance(predicted_score, float)
        self.assertGreater(predicted_score, current_runs)  # Check that predicted score is greater than current runs
