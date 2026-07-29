# One-page handover for a new hire

Project summary
---------------
CariSurg ED triage model and experiments (Weeks 1–8). This repository contains the data preprocessing, feature engineering, model training pipeline and experimental artifacts for model selection. The goal: reproducible pipeline so a new hire can run training from a single config file and reproduce the pinned model.

Final model decision
--------------------
Pinned model: Logistic Regression
Hyperparameters: penalty=l2, C=1.0, solver=liblinear, random_state=42
Rationale: Logistic Regression achieved the highest Macro F1 in Week‑7 experiments (see docs/model-selection.md and docs/week-7-model-choice.md for the decision journal).

How to run
----------
1. Create a Python 3.10+ virtual environment and install pinned dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Ensure data is available at the path specified in config.yaml (data_path).

3. Run training:
   python scripts/train.py --config config.yaml

Where the data lives
--------------------
Data should be stored in the data/ directory (example path: data/triage_data.csv). This repo does not contain patient-level data — if you have restricted data, place it at the path defined by config.yaml. Ensure data governance approvals are in place before using sensitive files.

Known limitations
-----------------
- Assumes the dataset contains a `target` column and numeric feature columns; update src/features.py for domain-specific transformations.
- No model-card / formal clinical evaluation included; further validation and calibration required before deployment.
- Requirements are pinned for reproducibility; upgrade packages cautiously and re-run tests.

Contact
-------
For questions, contact the original author (repo owner) or the project lead listed in docs/.
