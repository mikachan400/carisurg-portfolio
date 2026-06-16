# Week 1 – Final Submission

## Problem Statement

Emergency department clinicians at Mercer General Hospital face variability in triage decision-making, which can lead to inconsistent patient prioritisation. In a resource-constrained Caribbean emergency department setting, existing AI-assisted triage models demonstrate strong performance but are often trained on limited datasets and lack validation across diverse populations. This project proposes a 12-week pilot to evaluate whether a machine learning model trained on local data can improve triage consistency and reduce variability in clinical decision-making.

---

## Paper 1

This paper investigates whether machine learning models can predict patient admission and 30-day mortality using data collected during emergency department triage (Tschoellitsch et al., 2023). The authors used a retrospective dataset of over 58,000 patients and applied models including neural networks and random forests. The models achieved strong predictive performance, with AUC-ROC values of approximately 0.842 for ward admission and 0.925 for 30-day mortality. These results indicate that machine learning can effectively support early clinical decision-making in emergency settings. However, the study is limited by its use of data from a single hospital, reducing the generalisability of the findings. Furthermore, while high AUC-ROC values indicate strong predictive accuracy, these metrics do not fully account for real-time decision-making constraints in emergency settings where speed and interpretability are critical.

---

## Paper 2

This paper investigates whether large language models can improve clinical reasoning by asking effective diagnostic questions under uncertainty (Li et al., 2025). The authors developed ALFA, a framework that aligns LLMs using structured attributes of good question-asking and trained models on the MediQ-AskDocs dataset. The approach significantly improved performance, reducing diagnostic errors by 56.6% compared to existing models. This highlights the potential of AI to enhance not only prediction but also reasoning in clinical decision-making. However, the system has only been evaluated in experimental settings and lacks validation in real-world clinical environments. This is particularly relevant to triage settings, where effective questioning and information gathering are critical for accurate patient prioritisation. Additionally, the reliance on controlled datasets raises questions about how well such models would perform in fast-paced and resource-limited clinical environments.

---

## Paper 3

This paper reviews the use of artificial intelligence in emergency department triage and its potential to improve clinical workflows (Eriten, 2024). It highlights that AI systems can increase speed, accuracy, and consistency in patient assessment while optimising resource allocation. These findings demonstrate that AI has practical value in addressing challenges such as overcrowding and limited resources in emergency departments. However, issues such as data privacy, algorithmic bias, and resistance from healthcare professionals limit implementation in real clinical settings. Furthermore, as a narrative review rather than a systematic analysis, the findings may be subject to selection bias, limiting the strength of its conclusions.

---

## Paper 4

This systematic review examines the application of artificial intelligence in triage during emergencies and disasters (Tahernejad et al., 2024). The authors analysed multiple studies and found that AI systems improve triage efficiency, enable real-time monitoring, and enhance resource allocation, particularly in high-pressure mass casualty scenarios. These findings highlight that AI can significantly improve large-scale emergency response. However, many systems remain in experimental or simulated environments, and challenges such as infrastructure limitations, training requirements, and data security concerns hinder widespread adoption. Moreover, the heavy reliance on simulated disaster scenarios raises concerns about the generalisability of these findings.

---

## Paper 5

This systematic review evaluates the performance of machine learning models in predicting the need for intensive care among patients during emergency department triage (Chen et al., 2023). The authors found that models such as gradient boosting, neural networks, and random forests demonstrate strong predictive performance, with AUC values ranging from 0.68 to 0.97. These results highlight that machine learning can effectively identify critically ill patients early and support prioritisation decisions in emergency settings. However, the review notes that existing studies are limited in number and lack high-quality prospective validation, restricting real-world applicability. In addition, variability in model performance across studies highlights the need for standardisation and robust validation before clinical implementation.

---

## Gap Analysis and Literature Synthesis

The reviewed literature consistently demonstrates that artificial intelligence and machine learning models can improve triage accuracy, predict patient outcomes, and support clinical decision-making in emergency settings. Several studies show strong predictive performance, particularly in identifying high-risk patients and improving resource allocation (Tschoellitsch et al., 2023; Chen et al., 2023). Additionally, advancements in AI reasoning highlight the potential for more intelligent and adaptive decision-support systems (Li et al., 2025).

However, despite these promising results, significant gaps remain. First, many models are developed using retrospective or single-centre datasets, limiting their generalisability across diverse healthcare environments (Tschoellitsch et al., 2023). Second, a large proportion of studies are conducted in experimental or simulated settings, with limited validation in real-world clinical workflows (Tahernejad et al., 2024; Li et al., 2025). Third, implementation barriers such as data privacy concerns, lack of infrastructure, and resistance from healthcare professionals continue to hinder adoption in practice (Eriten, 2024). Tahernejad et al. (2024) similarly identify infrastructure and data security as barriers, although their analysis focuses more specifically on disaster and mass casualty contexts.

These gaps indicate that, while AI-based triage systems show strong theoretical and experimental performance, there is a critical need for real-world evaluation in specific healthcare contexts. Notably, none of the reviewed studies were conducted in Caribbean or comparable small-island developing state settings, highlighting a significant gap in the literature that this project seeks to address. This directly informs the proposed project, which aims to assess the use of a locally trained machine learning model in a Caribbean emergency department to improve triage consistency and ensure applicability across diverse patient populations.

---

## References

Tschoellitsch T, Seidl P, Böck C, Maletzky A, Moser P, Thumfart S, Giretzlehner M, Hochreiter S, Meier J. Using emergency department triage for machine learning-based admission and mortality prediction. *European Journal of Emergency Medicine*. 2023;30(6):408–416. doi:10.1097/MEJ.0000000000001068.

Li SS, Mun J, Brahman F, Ilgen JS, Tsvetkov Y, Sap M. ALFA: Aligning LLMs to Ask Good Questions – A Case Study in Clinical Reasoning. *arXiv*. 2025. doi:10.48550/arXiv.2502.14860.

Eriten S. Artificial intelligence-assisted triage in the emergency department: Current status and future perspectives. *Eurasian Clinical and Analytical Medicine*. 2024;12(Suppl 1):S30–S34. doi:10.4328/ECAM.10099.

Tahernejad A, Sahebi A, Salehi Sahl Abadi A, Safari M. Application of artificial intelligence in triage in emergencies and disasters: a systematic review. *BMC Public Health*. 2024;24:3203. doi:10.1186/s12889-024-20447-3.

Chen Y, Chen H, Sun Q, Zhai R, Liu X, Zhou J, Li S. Machine learning model identification and prediction of patients’ need for ICU admission: A systematic review. *American Journal of Emergency Medicine*. 2023;73:166–170. doi:10.1016/j.ajem.2023.08.043.

---

## AI Usage

This work was supported using Microsoft Copilot, Google Gemini, and Asta Allen AI to assist in summarising paper abstracts and organising content. All information was carefully reviewed and verified against the original sources to ensure accuracy.
