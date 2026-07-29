from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import time
import numpy as np


def train(df, config: dict, feature_cols, target_col):
    """Train a Logistic Regression model according to config and return metrics and model path."""
    cfg = config
    hp = cfg.get("model", {}).get("hyperparameters", {})
    test_size = cfg.get("train", {}).get("test_size", 0.2)
    rs = cfg.get("train", {}).get("random_state", 42)

    X = df[feature_cols].to_numpy()
    y = df[target_col].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=rs, stratify=y if len(np.unique(y))>1 else None)

    model = LogisticRegression(penalty=hp.get("penalty", "l2"), C=hp.get("C", 1.0), solver=hp.get("solver", "liblinear"), random_state=hp.get("random_state", 42), max_iter=1000)

    t0 = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - t0

    t1 = time.time()
    preds = model.predict(X_test)
    inference_time = time.time() - t1

    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "precision": float(precision_score(y_test, preds, average="macro", zero_division=0)),
        "recall": float(recall_score(y_test, preds, average="macro", zero_division=0)),
        "f1": float(f1_score(y_test, preds, average="macro", zero_division=0)),
        "train_time_seconds": train_time,
        "inference_time_seconds": inference_time,
    }

    return model, metrics


def save_model(model, path: str):
    joblib.dump(model, path)


def load_model(path: str):
    return joblib.load(path)
