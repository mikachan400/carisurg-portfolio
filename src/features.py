import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_features(df: pd.DataFrame, feature_cols: list):
    """Return (X, y) where X is scaled features and y is target column 'target'.

    This is a small, explicit feature-engineering function used by the pipeline.
    """
    X = df[feature_cols].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled
