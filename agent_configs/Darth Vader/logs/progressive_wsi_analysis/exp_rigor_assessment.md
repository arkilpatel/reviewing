### Claims-to-Experiments Mapping
1. **MSPN improves general MIL performance**: Supported by Table 1 (comparison across 4 frameworks, 3 FMs, 4 tasks).
2. **MSPN is computationally efficient**: Supported by Table 1 (Params/FLOPs), Figure 3, and Appendix F (Runtime scaling).
3. **MSPN is effective with pre-trained MIL models**: Supported by Table 2.
4. **Multiple scales progressively help**: Supported by Table 3 (Ablation on number of FOVs).

### Baseline Assessment
The baselines are strong and appropriate. The authors test across multiple widely adopted MIL frameworks (ABMIL, DSMIL, CLAM-SB, CLAM-MB) and compare against modern transformer-based methods (TransMIL, HAG-MIL). They also explicitly compare against alternative multi-scale fusion methods (Concatenation, Cross-Scale Attention). Furthermore, the usage of three state-of-the-art CPath foundation models (CONCH, GigaPath, UNI2) demonstrates robustness. The tuning budgets appear fair, with all models trained under standard cross-entropy / survival losses with equivalent epochs.

### Dataset Assessment
The datasets used are the NIHR BioResource Breast Cancer Dataset (491 cases) and SurGen (425 cases). While these are high-quality, real-world clinical datasets covering important tasks (ER, PR, HER2, and CRC Survival), the absolute number of WSIs (under 1,000 combined) is somewhat small for deep learning in CPath. This small sample size contributes to the high variance seen in the results. Contamination risk is low since the evaluation relies on standard 5-fold cross-validation.

### Metric Assessment
Metrics are appropriate: AUC for binary biomarker classification and C-index for survival prediction. Complementary metrics like F1-score or AUPRC would have been highly beneficial given that biomarker expression (e.g., HER2 positive) can often be imbalanced, but AUC is a standard starting point.

### Statistical Rigor
The authors report standard deviations obtained via 2000 bootstrap trials (Appendix E). This is a strong practice. However, they fail to perform strict statistical significance testing (e.g., paired t-tests or Wilcoxon signed-rank tests) between the baseline models and MSPN. Given that the standard deviations are relatively large (e.g., $\pm 2.0\%$ to $\pm 3.5\%$) and the performance gains are often in the $1.0\%$ to $4.0\%$ range, it is difficult to definitively conclude statistical significance for every task without explicit p-values.

### Ablation Assessment
The ablation study (Table 3) successfully isolates the impact of the number of FOVs (scales). Adding more scales generally improves performance, validating the progressive design. However, a critical ablation is missing: the paper does not isolate the *grid-based remapping* from the *CGN*. What happens if standard multi-scale inputs (actual 5x and 10x features) are fed into the CGN instead of the pseudo-coarse features from grid remapping? This would prove whether grid remapping is merely an efficiency trick or a superior representational choice.

### Missing Experiments
1. **Actual vs. Synthesized Multi-Scale**: An experiment comparing MSPN using actual 10x/5x extracted features versus MSPN using the 20x grid-remapped features.
2. **Pooling Strategy Ablation**: Comparing average pooling in the grid remapping step against max pooling or attention-based pooling.
3. **Statistical Significance Tests**: Explicit p-values for the performance deltas in Table 1.

### Error Analysis Assessment
Significant gaps exist here. The paper provides no systematic error analysis. It lacks an investigation into *when* or *why* the model fails (e.g., does it fail on borderline HER2 2+ cases?). Figure 4 shows qualitative successes, but no failure cases or adversarial examples are discussed.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

5.5
