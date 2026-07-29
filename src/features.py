import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np


def create_features(df: pd.DataFrame, feature_cols: list = None):
    """Return scaled feature matrix (numpy array).

    - If feature_cols is None, select numeric columns except 'target'.
    - Fills missing values with column median.
    - Returns numpy array of shape (n_samples, n_features).
    """
    df = df.copy()
    if feature_cols is None:
        feature_cols = [c for c in df.select_dtypes(include=["number"]).columns if c != "target"]

    # Ensure provided feature columns exist
    feature_cols = [c for c in feature_cols if c in df.columns]

    if len(feature_cols) == 0:
        raise ValueError("No feature columns available for create_features")

    X = df[feature_cols].copy()

    # Fill numeric NA values with median
    for c in X.columns:
        if X[c].isna().any():
            X[c] = X[c].fillna(X[c].median())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.values)
    return X_scaled
