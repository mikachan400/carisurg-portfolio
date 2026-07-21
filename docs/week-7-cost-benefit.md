# Week 7 Cost-Benefit Memo

**To:** Dr. De Freitas, Emergency Department Board, and Martina Griffith (Clinical IT Lead)

## Verdict

Based on benchmark performance, interpretability, and deployment considerations, I recommend retaining Logistic Regression as the preferred model for Phase 3 development. While more sophisticated models were evaluated, none demonstrated sufficient performance improvement to justify their additional complexity, computational cost, or reduced transparency.

---

## Background

Following the successful completion of the Week 6 baseline modelling exercise, the Emergency Department Board requested an evaluation of whether more advanced machine learning approaches would provide meaningful improvements in triage prediction performance.

The central question for this phase of the project was not simply whether a more complex model could be built, but whether the additional complexity would provide enough clinical value to justify the increased implementation and maintenance costs.

From an operational perspective, this evaluation required consideration of several competing priorities:

- Predictive performance
- Ability to identify clinically significant cases
- Computational cost
- Ease of deployment
- Interpretability for clinicians
- Long-term maintainability

These considerations are particularly important in healthcare settings where model decisions may have direct impacts on patient care and clinical workflows.

---

## Dataset and Methods

The Yale EMMLC Emergency Department triage dataset was used throughout this analysis. Each record represented an individual patient encounter and included a variety of clinical and administrative variables available during the triage process.

To ensure a fair comparison between models, the same train/test split established in Week 6 was reused throughout the evaluation. This prevented differences in performance from being attributed to changes in the data partition rather than differences in the modelling approach.

Several preprocessing steps were applied prior to model training, including:

- Data cleaning
- Missing-value handling
- Feature selection
- Feature engineering
- Scaling where appropriate

Additional engineered features were created using clinically relevant combinations of vital signs, including respiratory and oxygen-based indicators. Cross-validation and hyperparameter tuning techniques were also explored to optimise model performance.

The Week 6 Logistic Regression model served as the baseline against which all more complex models were measured.

The following advanced models were evaluated:

- Random Forest
- Tuned Random Forest
- Gradient Boosting
- Small Multi-Layer Perceptron (MLP)

---

## Benchmark Results

| Model | Macro F1 |
|---------|---------:|
| Logistic Regression (Baseline) | **0.468** |
| Small MLP | 0.402 |
| Random Forest (Tuned) | 0.399 |
| Gradient Boosting | 0.372 |
| Random Forest | 0.300 |

Macro F1 was selected as the primary comparison metric because it treats all ESI classes equally, including the rare but clinically important ESI Level 1 category.

The benchmark results demonstrated that none of the advanced models exceeded the performance of the baseline Logistic Regression model.

Although Macro F1 was used as the primary comparison metric, model selection was not based solely on predictive performance. Week 7 required consideration of the trade-off between accuracy, interpretability, computational cost, and deployability. Logistic Regression offered the strongest balance of these factors while also achieving the highest Macro F1 score in the benchmark.

---

## Arguments Supporting Logistic Regression

### 1. Strongest Overall Performance

Logistic Regression achieved the highest Macro F1 score of all evaluated models.

This finding is significant because the purpose of the Week 7 investigation was to determine whether additional model complexity would produce measurable performance gains. Despite the introduction of feature engineering, hyperparameter tuning, and alternative learning algorithms, the advanced models did not outperform the baseline.

From a purely empirical perspective, Logistic Regression remains the strongest-performing model tested within the current project scope.

### 2. High Interpretability

Interpretability is particularly important in clinical decision-support systems.

Logistic Regression allows clinicians and administrators to understand how different features influence model predictions. This transparency makes it easier to explain model outputs, validate behaviour, and build trust among healthcare staff.

By contrast, Random Forest, Gradient Boosting, and MLP models operate with substantially greater complexity. While techniques such as feature importance scores and SHAP values can provide insight, these approaches still require additional explanation and technical expertise.

A model that clinicians can understand is often more valuable than a marginally more accurate model that functions as a black box.

### 3. Lower Computational and Operational Costs

Logistic Regression has comparatively low computational requirements.

Training is fast, inference is efficient, and infrastructure requirements are minimal. This reduces deployment costs and simplifies maintenance.

From Martina Griffith's IT Governance perspective, lower computational demands translate into lower operational risk and lower infrastructure overhead.

Given that none of the advanced models delivered superior predictive performance, these additional costs cannot currently be justified.

---

## Arguments Against Logistic Regression

### 1. Limited Ability to Capture Complex Relationships

Logistic Regression assumes relatively simple relationships between features and outcomes.

Clinical data can contain complex, nonlinear interactions that may not be fully represented by a linear model. More advanced algorithms are generally better suited to discovering these patterns if they exist within the data.

Although Logistic Regression currently performs best, future datasets may contain relationships that favour more sophisticated approaches.

### 2. Potential Gains From Further Tuning

The advanced models evaluated during this phase were subject to reasonable optimisation, but they were not exhaustively tuned.

Additional experimentation with:

- Random Forest parameters
- Gradient Boosting configurations
- Neural network architectures
- Class-balancing strategies

may produce improved results.

The current findings should therefore be regarded as evidence for the present dataset and implementation rather than proof that advanced methods can never outperform Logistic Regression.

### 3. Continued Challenges With Rare Classes

All evaluated models, including Logistic Regression, continue to face challenges when predicting rare classes such as ESI Level 1.

From a patient-safety perspective, identifying critically ill patients remains one of the most important objectives of the triage system.

While Logistic Regression outperformed the alternatives overall, further work is required to improve minority-class performance and reduce the risk of under-triaging high-acuity patients.

---

## Risks and Unknowns

Several uncertainties remain:

- Additional hyperparameter tuning may improve advanced model performance.
- Larger datasets may favour more flexible machine learning methods.
- External validation has not yet been performed.
- Results are currently based on a single dataset and train/test split.
- Future feature engineering efforts may alter comparative performance.
- Operational deployment challenges have not yet been evaluated in a live clinical environment.
- Further optimisation may improve the performance of Random Forest, Gradient Boosting, or MLP models.

These uncertainties should be acknowledged when interpreting the benchmark results.

---

## Recommendation

At the current stage of development, the additional complexity introduced by Random Forest, Gradient Boosting, and Small MLP models does not provide sufficient benefit to justify adoption.

Logistic Regression achieved the strongest Macro F1 score, remained the most interpretable model, and requires the least computational overhead. These characteristics align closely with the needs of both clinical stakeholders and IT Governance.

For these reasons, I recommend that Logistic Regression remain the preferred model for Phase 3 development. Future work should focus on improving ESI Level 1 identification through additional feature engineering, class-balancing techniques, and further hyperparameter optimisation. More complex models should continue to be evaluated, but current evidence does not justify replacing the baseline model.

**Recommended Model for Phase 3: Logistic Regression.**
