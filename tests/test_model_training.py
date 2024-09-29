import unittest
import pandas as pd
from src.model_training import train_model
from src.data_preprocessing import preprocess_data, load_data


class TestModelTraining(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'runs': [10, 20, 30, 40],
            'balls': [6, 12, 18, 24],
            'batsmanName': ['A', 'B', 'C', 'D'],
            'out/not_out': ['not_out', 'out', 'not_out', 'out']
        }
        self.df = pd.DataFrame(data)

    def test_model_training(self):
        processed_df = preprocess_data(self.df)

        # Define feature columns (X) and target column (y)
        feature_columns = ['runs', 'balls']
        target_column = 'runs'

        X = processed_df[feature_columns]
        y = processed_df[target_column]

        # Train the model and assert it returns a trained model
        model = train_model(X, y)
        self.assertIsNotNone(model)
