# Week 5 Feasibility Memo Outline

## Verdict
Proceed with development of a baseline triage model.

## Dataset Summary
- 55,000+ encounters
- Adult emergency department patients
- 225 features
- Target variable: ESI

## Top 3 Concerns
1. Class imbalance
2. Outcome leakage
3. External validity

## Top 3 Reasons to Proceed
1. Large dataset
2. Rich clinical data
3. Complete target labels

## Caveats
- US-based dataset
- Sparse complaint variables
- Underrepresentation of ESI-1

## Candidate Features
- Age
- Heart rate
- Respiratory rate
- Oxygen saturation
- Blood pressure
- Temperature
- Glucose
- Chest pain
- Shortness of breath
- Arrival mode
