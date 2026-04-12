### Claims-to-Experiments Mapping
- **Claim:** Neon works across model families. **Support:** Experiments on Diffusion (EDM-VP), Flow Matching, AR (xAR, VAR), and Few-step (IMM).
- **Claim:** Minimal compute overhead. **Support:** Fine-tuning budget explicitly tracked in all main Figures (3, 5, 7), showing optimal convergence in < 2-3 Mi images.
- **Claim:** Precision-recall trade-off mechanism. **Support:** Fig 4 and 6 explicitly plot precision vs. recall against merge weight $w$.
- **Claim:** Transferability across architectures. **Support:** Fig 8 ablates cross-architecture data sources.

### Baseline Assessment
- **Appropriate and Strong:** The authors apply Neon to highly competitive and recent SOTA baselines (e.g., xAR-L, EDM2, VAR-d16/d30, IMM). They compare their post-hoc enhancements to other strong post-hoc methods like SIMS, DDO, and Discriminator Guidance.
- **Fairness:** The authors use the exact official pre-trained checkpoints and report the extra NFE/compute explicitly. The performance gains are measured against the fully trained base models.

### Dataset Assessment
The experiments utilize standard, high-difficulty generative benchmarks: CIFAR-10, FFHQ-64, ImageNet-256, and ImageNet-512. The datasets are appropriate and sufficiently diverse.

### Metric Assessment
The authors report FID as the primary quality metric, which is community standard. Crucially, they supplement this with Precision and Recall metrics, which are perfectly suited to validate their specific theoretical claims about mode redistribution.

### Statistical Rigor
- The authors utilize a joint grid search over $w$ and CFG scale $\gamma$ to ensure they find the optimal operating point.
- The use of 10k samples for search and 50k samples for the final FID report is standard practice.
- The U-shaped curves observed across multiple independent runs and architectures demonstrate the stability of the phenomenon.

### Ablation Assessment
- **Cross-Architecture Transfer:** Excellent ablation (Fig 8) showing that degradation signals can be transferred from Flow to Diffusion, confirming the theoretical uniformity of the mode-seeking bias.
- **Out-of-Distribution Data:** Ablating with CIFAR-10C to prove that the signal requires self-generated mode-collapse, not just arbitrary noise/corruptions.
- **Base Model Quality:** Fig 9 tests Neon on artificially weakened base models (trained on subsets of CIFAR-10), proving it doesn't strictly require near-optimal $\theta^*$.
- **Synthetic Data Quality:** Fig 10 shows Neon is robust to the CFG scale used during synthetic data generation.

### Missing Experiments
- The evaluation is extremely thorough. A potential addition would be qualitative (human) evaluation to confirm the FID improvements map to visually noticeable realism/diversity improvements, particularly given the known flaws of FID. However, the use of precision-recall somewhat mitigates this.

### Error Analysis Assessment
The paper characterizes the failure regime elegantly via the theory and toy experiments: it explicitly identifies that Neon *fails* (and standard self-training succeeds) when samplers are diversity-seeking instead of mode-seeking (Appendix B.9).

### Overall Experimental Rigor Verdict
Rigorous. The experimental design perfectly isolates the claims, uses strong modern baselines, and includes insightful ablations that validate the theoretical edge cases.