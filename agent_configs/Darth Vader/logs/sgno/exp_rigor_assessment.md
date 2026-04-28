### Claims-to-Experiments Mapping
- **Claim 1 (Superior long-horizon stability)**: Supported by Table 1 (GMean100) and Figures 2/3, but the baselines are weak.
- **Claim 2 (Importance of residual pathways)**: Supported by Table 2, which ablates $\alpha_w=0$ and $\alpha_g=0$.
- **Claim 3 (Non-positive constraint stabilizes rollouts)**: **UNSUPPORTED.** There is absolutely no ablation showing what happens if the `-softplus` constraint on the real part of the generator is removed. This is the core novelty of the paper, yet it is completely untested.

### Baseline Assessment
- **Missing Strong Baselines**: The paper compares SGNO against vanilla architectures (Conv, Res, UNet, Dil, FNO). It completely fails to compare against existing *stabilized* neural operators explicitly designed for long-horizon rollouts, such as IFNO, iUFNO, IAFNO, SSNO, or PDE-Refiner, despite citing them. Evaluating a "stable" neural operator only against vanilla, un-stabilized baselines is a fundamentally flawed experimental design.

### Dataset Assessment
- The use of APEBench is appropriate. However, the authors only evaluate on a 7-task subset of APEBench, rather than the full suite. It is unclear if these 7 tasks were cherry-picked. 

### Metric Assessment
- GMean100 and stable-step CDFs are reasonable metrics for assessing long-horizon rollout degradation.

### Statistical Rigor
- The authors follow the APEBench protocol (50 seeds for 1D, 20 for 2D/3D), reporting medians. This is standard and acceptable.

### Ablation Assessment
- **Fundamentally Flawed**: The ablation study (Table 2) only tests disabling the entire forcing injection ($\alpha_g=0$) or pointwise correction ($\alpha_w=0$). It completely misses the most critical ablation: removing the non-positive constraint on the real part of the spectral generator. Without this ablation, there is no empirical evidence that the specific non-positive constraint—the paper's main methodological contribution—is actually responsible for the improved stability. They also do not ablate the spectral masking.

### Missing Experiments
1. Comparison against state-of-the-art *stable* neural operators (e.g., IFNO, PDE-Refiner).
2. An ablation removing the `-softplus` constraint on $\Re(\lambda)$.
3. An ablation removing the spectral mask $\mathcal{F}(k)$.
4. Empirical measurement of the Lipschitz constants or the $q(\delta t)$ amplification factor during training and inference to see if the model naturally satisfies the theoretical bounds without explicit regularization.

### Error Analysis Assessment
- Very minimal. The paper shows aggregate CDFs and a couple of trajectory plots, but lacks a deep analysis of *why* the model fails when it eventually does, or how the learned spectral generators behave across different modes.

### Overall Experimental Rigor Verdict
Significant gaps

### Experimental Rigor Score: 3
