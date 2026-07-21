# Week 7 Model Choice Decision

## Context

- Week 6 established Logistic Regression as the baseline triage model.
- Week 7 required evaluation of more complex alternatives and consideration of deployment trade-offs.

## Alternatives Considered

- Random Forest
- Tuned Random Forest
- Gradient Boosting
- Small Multi-Layer Perceptron (MLP)

## Decision

Logistic Regression remains the recommended model for Phase 3 development.

## Reasoning

- Achieved the highest Macro F1 score (0.468).
- Most interpretable model for clinical stakeholders.
- Lowest computational and deployment complexity.
- Advanced models did not outperform the baseline.

## What I Do Not Know Currently

- Whether additional hyperparameter tuning could improve advanced model performance.
- Whether these results would generalise to external emergency department datasets.
