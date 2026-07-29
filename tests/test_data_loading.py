import pandas as pd
from src.data import clean

def test_data_loading_and_schema(tmp_path):
    # create a small CSV with expected columns
    df = pd.DataFrame({
        'f1': [1,2,3],
        'f2': [4,5,6],
        'target': [0,1,0]
    })
    p = tmp_path / "mini.csv"
    df.to_csv(p, index=False)

    df_loaded = pd.read_csv(p)
    df_clean = clean(df_loaded)

    assert 'target' in df_clean.columns
    assert df_clean.shape[0] == 3

