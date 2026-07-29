#!/usr/bin/env python3
import argparse
from pathlib import Path
import joblib
import json

from src.utils import load_config, ensure_dir
from src.data import load_raw, clean
from src.features import create_features
from src.model import train, save_model


def main(config_path: str):
    cfg = load_config(config_path)
    data_path = cfg.get("data_path")
    artifacts = cfg.get("artifacts_path", "artifacts/")
    ensure_dir(artifacts)

    df = load_raw(data_path)
    df = clean(df)

    # NOTE: adjust feature_cols/target_col to your dataset columns
    # For the smoke pipeline we assume the dataset has numeric features named f1..f5 and 'target'
    possible_features = [c for c in df.columns if c.startswith("f")]
    if len(possible_features) == 0:
        # fallback: use all columns except 'target'
        feature_cols = [c for c in df.columns if c != "target"]
    else:
        feature_cols = possible_features

    target_col = "target"
    if target_col not in df.columns:
        raise KeyError(f"Expected target column '{target_col}' in data")

    X = create_features(df, feature_cols)
    model, metrics = train(df, cfg, feature_cols, target_col)

    model_path = Path(artifacts) / "model.joblib"
    save_model(model, model_path)

    metrics_path = Path(artifacts) / "metrics.json"
    with metrics_path.open("w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Trained model saved to {model_path}")
    print(f"Metrics saved to {metrics_path}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True, help="Path to config.yaml")
    args = p.parse_args()
    main(args.config)
