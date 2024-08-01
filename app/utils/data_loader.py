# app/utils/data_loader.py
import pandas as pd

def load_data(file_path: "data/dataset.csv"):
    """
    Load dataset from a CSV file.
    
    Parameters:
    - file_path (str): Path to the CSV file containing the dataset.

    Returns:
    - data (pd.Series): Series of text data.
    - labels (pd.Series): Series of labels corresponding to the text data.
    """
    data_frame = pd.read_csv(file_path)

    return data_frame["text"], data_frame["label"]
