### Claims-to-Experiments Mapping
- Claim: Structural features fail to detect LLM graphs -> Supported by RF on graph properties (Tables 1, 4) and GNNs on graph properties (Tables 3, 6).
- Claim: Embeddings succeed -> Supported by RF on embeddings (Tables 2, 5, 8) and GNNs on embeddings (Tables 3, 6, 10).
- Claim: Driven by semantics, not dimensionality -> Supported by Random-vector control and PCA-k ablation (Figures 15, 16).
- Claim: Generalizes across models -> Supported by cross-model experiment (Tables 9, 10).

### Baseline Assessment
Appropriate and rigorous. They evaluate:
1. Ground truth (human).
2. GPT-4o.
3. Claude 3.5 Sonnet.
4. Field-matched random baseline.
5. Temporally-ordered random baseline.
6. Subfield random baseline.
This is an exhaustive set of control baselines to ensure the models aren't just learning trivial artifacts.

### Dataset Assessment
10,000 focal papers from SciSciNet (~275k references) is a large, representative dataset that avoids the small-N problem common in LLM evaluation.

### Metric Assessment
Accuracy and F1-score are standard and appropriate for balanced binary/ternary classification tasks.

### Statistical Rigor
Excellent. Results are reported as means ± standard deviations over 10 random seeds. A saturation analysis (Wasserstein distance) is also provided.

### Ablation Assessment
The paper includes robust ablations: random-vector control, PCA dimensionality ablation, and evaluating isolated node semantic roles.

### Missing Experiments
None of significance. The pipeline is comprehensive.

### Error Analysis Assessment
The cross-model experiment and semantic role visualizations serve as good qualitative and analytical checks on the model's behavior.

### Overall Experimental Rigor Verdict
Rigorous. The paper is exceptionally well-designed empirically.