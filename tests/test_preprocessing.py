import unittest
import pandas as pd
from src.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        data = {
            'runs': [10, 20, 30, 40],
            'balls': [6, 12, 18, 24],
            'batsmanName': ['A', 'B', 'C', 'D'],
            'out/not_out': ['not_out', 'out', 'not_out', 'out']
        }
        self.df = pd.DataFrame(data)

    def test_preprocess_data(self):
        processed_df = preprocess_data(self.df)
        expected_run_rate = pd.Series([1.0, 1.0, 1.0, 1.0])  # Expected run rate as a Pandas Series
        pd.testing.assert_series_equal(processed_df['run_rate'], expected_run_rate)
