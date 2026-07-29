import pandas as pd
from src.model import train
from ruamel.yaml import YAML
import tempfile


def test_training_smoke(tmp_path):
    # create ~50 rows of synthetic numeric data
    n = 60
    df = pd.DataFrame({
        'f1': pd.np.random.rand(n),
        'f2': pd.np.random.rand(n),
        'target': [0 if i < n/2 else 1 for i in range(n)]
    })

    # simple config dict mimicking loaded YAML
    cfg = {
        'model': {
            'hyperparameters': {
                'penalty': 'l2',
                'C': 1.0,
                'solver': 'liblinear',
                'random_state': 42
            }
        },
        'train': {
            'test_size': 0.2,
            'random_state': 42
        }
    }

    feature_cols = ['f1', 'f2']
    model, metrics = train(df, cfg, feature_cols, 'target')

    assert 'f1' in df.columns
    assert isinstance(metrics.get('f1'), float) or isinstance(metrics.get('f1'), (float,))
