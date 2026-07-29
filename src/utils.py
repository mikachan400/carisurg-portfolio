import yaml
from pathlib import Path

def load_config(path: str):
    path = Path(path)
    with path.open("r") as f:
        cfg = yaml.safe_load(f)
    return cfg


def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
