### Claimed Contributions
1. A comprehensive evaluation framework for robustness in TAGs covering GNNs, RGNNs, and GraphLLMs.
2. Empirical insights including the text-structure robustness trade-off, the revitalization of simple RGNNs with advanced encoders, and the poisoning vulnerability of GraphLLMs.
3. SFT-auto, a novel defense framework utilizing a multi-task training and detection-prediction pipeline.

### Prior Work Assessment
- **Evaluation Framework:** Prior works (GRB, TrustGLM, etc.) evaluated GNNs or GraphLLMs in fragmented settings (either evasion or poisoning, limited attacks). This paper's delta is **Substantial** because it unifies these disparate paradigms under a single, large-scale (10 datasets, 4 domains) threat model.
- **Empirical Insights:** The text-structure trade-off is a novel and valuable framing. While vulnerabilities of individual models were known, formally identifying this dichotomy across architectures is a **Substantial** new insight.
- **SFT-auto:** Using LLMs for anomaly detection and adaptive prediction is an **Incremental to Moderate** methodological extension of standard instruction tuning, but its application to solve this specific trade-off is creative and effective.

### Novelty Verdict
Substantial. 

### Justification
While the individual components (GNNs, LLMs, adversarial attacks) are well-studied, the comprehensive synthesis and the resulting insights (particularly the trade-off and the role of text encoders in RGNNs) represent a significant conceptual advance for the field of robust graph learning. 

**Novelty Score: 7.5 / 10**