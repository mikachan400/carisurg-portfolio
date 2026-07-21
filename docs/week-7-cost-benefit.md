Week 7 Cost-Benefit Memo

To: Dr. De Freitas, Emergency Department Board, and Martina Griffith (Clinical IT Lead)

Verdict

Based on benchmarking performance, interpretability, and deployment considerations, I recommend retaining Logistic Regression as the preferred model for Phase 3 development.

Dataset and Methods

The Yale EMMLC emergency department triage dataset was used to predict Emergency Severity Index (ESI) levels. To ensure a fair comparison, all models were trained and evaluated using the same train/test split established in Week 6.

The Week 6 Logistic Regression baseline was compared against several more complex models:

Random Forest
Tuned Random Forest
Gradient Boosting
Small Multi-Layer Perceptron (MLP)

Feature engineering, cross-validation, and hyperparameter tuning techniques were applied where appropriate.

Benchmark Results
Model	Macro F1Logistic Regression (Baseline)	0.468
Small MLP	0.402
Random Forest (Tuned)	0.399
Gradient Boosting	0.372
Random Forest	0.300
Arguments Supporting Logistic Regression
1. Strongest Overall Performance

Logistic Regression achieved the highest Macro F1 score of all evaluated models. None of the more sophisticated models surpassed the baseline, despite requiring greater complexity.

2. High Interpretability

Logistic Regression remains easy to explain to clinical stakeholders. Individual model predictions can be linked to feature weights, making the model easier to audit and trust.

3. Lower Computational Cost

Compared with Random Forest, Gradient Boosting, and MLP models, Logistic Regression requires fewer computational resources for training and inference. This reduces deployment complexity and operational costs.

Arguments Against Logistic Regression
1. Limited Ability to Model Complex Relationships

Logistic Regression assumes relatively simple relationships between inputs and outputs and may fail to capture complex interactions present in clinical data.

2. Potential Future Ceiling

More advanced models may outperform Logistic Regression if additional tuning, feature engineering, or larger datasets become available.

3. Continued Challenges with Rare Classes

While Logistic Regression performed best overall, identifying rare and clinically significant ESI Level 1 patients remains challenging.

Risks and Unknowns
Additional hyperparameter tuning may improve Random Forest or Gradient Boosting performance.
External validation has not yet been performed.
Results are based on a single dataset and train/test split.
Future data collection may favour different model architectures.
Recommendation

Although more sophisticated models were explored, none provided sufficient performance improvement to justify the increased complexity. Logistic Regression achieved the strongest Macro F1 score while remaining interpretable, computationally efficient, and easier to deploy. I therefore recommend Logistic Regression as the preferred model for Phase 3 development.
