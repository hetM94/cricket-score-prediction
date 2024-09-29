import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Ensure you're working with a copy of the dataframe
    df = df.copy()

    # Convert 'runs' and 'balls' to numeric, coercing invalid values to NaN
    df['runs'] = pd.to_numeric(df['runs'], errors='coerce')
    df['balls'] = pd.to_numeric(df['balls'], errors='coerce')

    # Drop rows where 'runs' or 'balls' are NaN
    df = df.dropna(subset=['runs', 'balls'])

    # Replace 0 balls with 1 to avoid division by zero in run_rate calculation
    df['balls'] = df['balls'].replace(0, 1)

    # Create 'run_rate' feature
    df['run_rate'] = df['runs'] / (df['balls'] / 6)  # Convert balls to overs

    # Handle categorical variables
    df['batsmanName'] = pd.factorize(df['batsmanName'])[0]
    df['out/not_out'] = df['out/not_out'].apply(lambda x: 1 if x == 'out' else 0)

    # Fill or drop missing values in other features as needed (ensure no NaNs remain)
    df = df.fillna(0)  # Filling NaN values with 0 (or another appropriate value)

    # Remove any rows with infinity values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    return df

if __name__ == "__main__":
    file_path = '../data/t20.csv'
    df = load_data(file_path)
    df = preprocess_data(df)
    print(df.head())
