import pandas as pd
from pathlib import Path

def load_raw(path: str) -> pd.DataFrame:
    """Load CSV from path into a DataFrame.

    Expects a CSV with a header row. Returns raw DataFrame.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: lower-case column names, drop fully NA cols.

    Add or adapt this to the project-specific cleaning steps.
    """
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    # drop columns that are all NA
    df = df.dropna(axis=1, how="all")
    return df
