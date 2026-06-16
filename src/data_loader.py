import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print(f"Loaded: {path} | Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None