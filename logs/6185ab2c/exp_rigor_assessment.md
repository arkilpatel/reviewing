### Claims-to-Experiments Mapping
- **Trade-off:** Supported by extensive comparisons across GNNs, RGNNs, and GraphLLMs under both structural and textual attacks.
- **RGNN Revitalization:** Supported by baseline comparisons using RoBERTa embeddings.
- **SFT-auto Effectiveness:** Supported by ablation studies (vs noise-injection and similarity-filtering) and main results.

### Baseline Assessment
Extremely strong. The paper compares 13 GNN/RGNN baselines (including GCN, GAT, APPNP, GPRGNN, RobustGCN, GCORN, NoisyGCN, GRAND, SoftmedianGDC, EvenNet, ElasticGNN, GNNGuard, RUNG) and several GraphLLM baselines (LLaGA, GraphGPT, SFT-neighbor). The inclusion of so many recent and classic baselines is commendable.

### Dataset Assessment
Excellent. 10 datasets across 4 domains (academic, web, social, e-commerce) provide a highly robust and diverse testbed, avoiding overfitting to specific graph types.

### Metric Assessment
Appropriate. Accuracy under attack, relative accuracy drop, and average rank across datasets provide a clear and multi-faceted view of robustness.

### Statistical Rigor
High. Results are reported with standard deviations across 3 independent runs. The perturbation ratios are sufficiently high to distinguish real robustness from clean accuracy artifacts.

### Ablation Assessment
Strong. The paper thoughtfully ablates alternative GraphLLM defense strategies (noise injection, similarity filtering) and shows why they fail to break the trade-off, strongly justifying the SFT-auto design.

### Missing Experiments
None of significance. The evaluation is one of the most thorough in recent graph robustness literature.

### Overall Experimental Rigor Verdict
Rigorous. The experimental design is exemplary.

**Experimental Rigor Score: 9.0 / 10**