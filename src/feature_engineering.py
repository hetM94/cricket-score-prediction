def feature_engineering(df):
    x = df[['runs', 'balls', 'battingPos', '4s', '6s', 'run_rate']]
    y = df['runs']  # Target: Total runs scored by the batsman
    return x, y

if __name__ == "__main__":
    from data_preprocessing import preprocess_data, load_data
    df = preprocess_data(load_data('../data/t20.csv'))
    x, y = feature_engineering(df)
    print(x.head())
