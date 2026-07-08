# AI-Assisted Emergency Department Triage Dataset Feasibility Assessment

## Verdict
**Proceed with development of a baseline triage model, with caveats.** The dataset contains sufficient volume, clinical detail, and target labels to support baseline model development. However, class imbalance, potential outcome leakage, and limited Caribbean external validity should be addressed before clinical deployment.

---

## Dataset Summary
The dataset contains more than 55,000 adult emergency department encounters and approximately 225 features per patient. Variables include demographic information, arrival characteristics, triage vital signs, and a large collection of chief complaint indicators. The target variable is the Emergency Severity Index (ESI), a five-level triage classification system ranging from ESI 1 (most urgent) to ESI 5 (least urgent).

The dataset provides information typically available during triage and therefore represents an appropriate foundation for artificial intelligence-assisted decision support. Data quality assessment revealed relatively low missingness among structured variables, reducing the need for extensive imputation and supporting model feasibility.

![Figure 1 – Missingness Heatmap](images/missingness_heatmap.png)

---

## Top 3 Quality Concerns

### 1. Class Imbalance
The most significant challenge identified is the imbalance across ESI categories. ESI 1 encounters represent only a very small proportion of all patient presentations. This imbalance may reduce the model's ability to recognise critically ill patients because relatively few examples are available during training.

> **Mitigation:** Potential approaches include class weighting, stratified sampling, targeted oversampling techniques, and separate evaluation of ESI 1 performance. Model performance should be monitored specifically for high-acuity patients because errors in these cases carry the greatest clinical risk.

![Figure 2 – ESI Distribution](images/esi_distribution.png)

### 2. Outcome Leakage
Variables such as `disposition` and `previousdispo` become known only after triage and therefore should not be used as model inputs. Using such variables would introduce information that would not be available at the time of prediction and could falsely inflate model performance.

> **Mitigation:** These variables should be excluded from model training and reserved only for exploratory analysis.

### 3. External Validity
The dataset originates from a United States emergency department and may not fully represent Caribbean healthcare systems, patient populations, disease prevalence, resource limitations, or clinical workflows.

> **Mitigation:** Future validation using Caribbean emergency department data is recommended before implementation in local clinical environments.

---

## Top 3 Reasons to Proceed

1. **Large Dataset:** The dataset contains more than 55,000 emergency department encounters, providing a substantial amount of information for baseline model development.
2. **Real Clinical Triage Labels:** The ESI labels represent actual triage decisions made by healthcare professionals, providing an appropriate target for supervised machine learning.
3. **Rich Clinical Information:** The dataset incorporates demographics, arrival information, physiological measurements, and chief complaints. Together these variables capture many factors used by clinicians during triage decision-making.

---

## ESI-1 Analysis and Feature Importance
Although ESI 1 patients are underrepresented, they remain clinically important because they represent the highest-acuity presentations. 

Analysis of ESI 1 encounters suggests that high-risk complaints such as respiratory distress, chest pain, altered mental status, unresponsiveness, and other emergency presentations are disproportionately represented among these patients. This indicates that chief complaint data may provide important predictive signals alongside physiological measurements.

The rarity of ESI 1 encounters highlights the need for careful model evaluation to ensure critically ill patients are not overlooked.

---

## Top 10 Feature Shortlist
The following variables were selected using clinical reasoning and exploratory correlations with ESI level.

| Rank | Feature | Clinical Justification |
| :---: | :--- | :--- |
| **1** | Age | Older patients are more likely to present with complex and high-risk conditions. |
| **2** | Oxygen Saturation (`triage_vital_o2`) | Low oxygen saturation may indicate respiratory or cardiovascular compromise. |
| **3** | Respiratory Rate (`triage_vital_rr`) | Respiratory rate is often an early indicator of deterioration. |
| **4** | Heart Rate (`triage_vital_hr`) | Abnormal heart rates may indicate physiological instability. |
| **5** | Systolic Blood Pressure (`triage_vital_sbp`) | Blood pressure abnormalities may indicate circulatory compromise. |
| **6** | Chest Pain (`cc_chestpain`) | Frequently associated with potentially life-threatening cardiovascular conditions. |
| **7** | Shortness of Breath (`cc_shortnessofbreath`) | Common in serious respiratory and cardiac emergencies. |
| **8** | Altered Mental Status (`cc_alteredmentalstatus`) | Suggests neurological, metabolic, or systemic emergencies. |
| **9** | Arrival Mode (`arrivalmode`) | Ambulance arrivals often represent higher-acuity patients. |
| **10** | Glucose (`triage_glucose`) | Abnormal glucose levels may indicate significant metabolic disturbances. |

---

## Should Synthetic Data Be Used?
The use of synthetic data should be approached cautiously.

While synthetic oversampling methods may help address the scarcity of ESI 1 encounters, these patients represent some of the most clinically complex and high-risk cases within the dataset. Artificially generated encounters may not adequately capture the complexities of real emergency presentations and could introduce unrealistic clinical patterns.

At this stage, safer approaches include class weighting, careful evaluation of model performance for ESI 1 patients, and collection of additional real-world data. Synthetic methods should only be considered if clinically validated.

---

## Dashboard Summary
Several visualisations were generated to assess data quality and modelling feasibility.

* **Figure 1 – Missingness Heatmap:** Demonstrated high completeness across structured variables.
* **Figure 2 – ESI Distribution:** Highlighted substantial class imbalance and the scarcity of ESI 1 patients.
* **Figure 3 – Race and Ethnicity Distribution:** Provided demographic context and informed fairness considerations.
* **Figure 4 – Top Chief Complaints:** Identified the most common presenting complaints.
* **Figure 5 – Vitals by ESI Level:** Demonstrated separation between acuity categories based on physiological measurements.
* **Figure 6 – Correlation Analysis:** Identified relationships between clinical features and triage severity.

---

## Caveats
* The dataset originates from a United States healthcare setting.
* ESI 1 encounters are severely underrepresented.
* Many chief complaint variables are sparse.
* Correlations do not imply causation.
* Caribbean external validity has not yet been established.

---

## Conclusion
Overall, the dataset is suitable for development of a baseline emergency department triage model. The dataset contains a large number of encounters, clinically relevant variables, and complete triage labels. Model development should proceed while accounting for class imbalance, outcome leakage, and external validity concerns.

Future work should focus on baseline model development, performance evaluation across all ESI levels, and validation using Caribbean clinical data.
