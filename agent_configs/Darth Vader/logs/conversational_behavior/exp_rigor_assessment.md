# Empirical Rigor Assessment

## 1. Experimental Design
The evaluation of the Speech Act Perceiver uses ConversationGoT-120h (in-domain) and Candor (OOD). However, the baseline suite is critically deficient. There are no external baselines for speech act detection (e.g., standard frozen LLMs, fine-tuned RoBERTa/BERT, or specialized turn-taking models). The "robust behavior detection" claim relies entirely on the absolute F1/AUC numbers without comparing against state-of-the-art.

## 2. Evaluation Metrics and Quality
The use of AUC alongside F1 is appreciated given the class imbalance. However, the reported F1 scores for critical full-duplex classes are very low even in-domain (Directives 0.474, Commissives 0.474, Interruption 0.495, Backchannel 0.560). A foundation model that fails to achieve 0.6 F1 on its own training distribution's core tasks cannot be considered robust. Furthermore, the GoT rationale generation is evaluated using GPT-4o as a judge. Evaluating a system trained on GPT-4o/5 outputs using GPT-4o introduces extreme self-preference bias. 

## 3. Reproducibility
The authors describe the training parameters (AdamW, 15 epochs, batch size 8) and dataset construction cleanly. But the reliance on proprietary GPT-4o/5 for data generation and the lack of human inter-annotator agreement (Cohen's Kappa) for the labels severely compromise the scientific rigor of the dataset.

## 4. Significance and Statistical Validation
The OOD transfer to Candor shows modest degradation, which is a positive signal. However, the rationale generation (the core "GoT" component) is never evaluated on the OOD real-world data; Table 7 only reports scores presumably on the synthetic test set. This leaves the core contribution untested on real human data.

## Score
Score: 3
