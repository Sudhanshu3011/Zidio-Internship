import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_input(data):
    """
    Preprocess the input data to match the format used during training.
    
    Args:
        input_data (dict): Raw input data from the form or live source.
    
    Returns:
        pd.DataFrame: Cleaned and encoded data ready for prediction.
    """
    df = pd.DataFrame([input_data])
    
    # Encoding categorical features (example: "type")
    if 'type' in df.columns:
        le = LabelEncoder()
        df['type'] = le.fit_transform(df['type'])
    
    # Fill missing values (if any)
    df.fillna(0, inplace=True)
    
    return data
