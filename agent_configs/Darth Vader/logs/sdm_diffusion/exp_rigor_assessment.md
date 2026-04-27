# Experimental Rigor & Evaluation Evaluator

### Claims-to-Experiments Mapping
- **Claim:** Adaptive solver improves efficiency by using Euler early and Heun later. -> Supported by Table 1 (SDM Adaptive Solver row).
- **Claim:** Adaptive scheduling improves quality by bounding Wasserstein error. -> Supported by Table 1 (SDM Adaptive Scheduling row).
- **Claim:** Combining both methods yields the best overall trade-off. -> Supported by Table 1 (SDM row).
All major claims are backed by corresponding experimental setups.

### Baseline Assessment
The authors primarily compare against EDM (Karras et al., 2022) and COS (Williams et al., 2024). 
- **Significant Gap in Baselines:** The paper completely omits comparisons against modern, fast, higher-order solvers. While the authors cite exponential integrators like DPM-Solver++ (Lu et al., 2025) and UniPC (Zhao et al., 2023) in their introduction, they do not evaluate against them. DPM-Solver++ is widely considered the state-of-the-art for sampling in the 10-30 step regime. Comparing a new solver/scheduler only against EDM's heuristic schedule and COS, while completely ignoring the most prominent fast solvers used by the community, severely weakens the empirical claim of achieving "state-of-the-art performance." Furthermore, DPM-Solver possesses an adaptive step-size variant that would serve as a perfectly matched, direct baseline.

### Dataset Assessment
The datasets (CIFAR-10, FFHQ, AFHQv2, ImageNet 64x64) are standard and appropriate for foundational diffusion model evaluation. However, the resolutions are quite small (32x32 and 64x64) by modern standards. Testing on higher resolutions (e.g., ImageNet 256x256 or Latent Diffusion models) would have provided much stronger evidence for the scalability of the proposed method.

### Metric Assessment
FID and NFE are the standard metrics for this task and match the claims well. However, evaluating sample quality solely on FID can sometimes be misleading, especially when differences are microscopic (e.g., 1.96 vs 1.93). A complementary metric like Inception Score (IS) or precision/recall would have added robustness.

### Statistical Rigor
- **Critical Flaw in Variance Reporting:** Statistical variance reporting is entirely absent from the paper. Generating samples from diffusion models inherently involves randomness due to the initial noise vector $x_T$. FID scores on CIFAR-10 can easily vary by $\pm 0.05$ to $0.1$ purely due to the random seed used to generate the 50k samples. The improvements shown by SDM (e.g., reducing FID from 1.96 to 1.93 on CIFAR-10) are extremely small and highly likely to fall within the margin of error or standard deviation of the metric. Without reporting error bars, standard deviations, or results averaged across multiple random seeds, it is scientifically impossible to determine if a drop of 0.03 in FID is statistically significant or merely noise.

### Ablation Assessment
The ablations are well-designed and thorough. The authors successfully isolate the effect of the adaptive solver, the adaptive schedule, the choice of switching threshold $\tau_k$ (Figure 4), and the schedule function $\Lambda(t)$ (Table 5). This factorial design clearly demonstrates the independent and combined contributions of the proposed components.

### Missing Experiments
1. **Direct comparison against DPM-Solver++ and UniPC**, specifically the adaptive step-size variants.
2. **Error bars / standard deviation** across multiple random seeds for all reported FID scores.
3. **High-resolution image generation** (e.g., Stable Diffusion / LDM) to prove the curvature proxy holds and scales efficiently in latent spaces.

### Error Analysis Assessment
The paper includes a strong analytical experiment showing the local Wasserstein error bound $\eta_t$ over time (Figure 3), which provides excellent insight into *why* the method outperforms the EDM schedule (by allocating more error budget to early stages). However, there is no qualitative failure case analysis or discussion of regimes where the delayed curvature estimator fails to switch solvers in time.

### Overall Experimental Rigor Verdict
Mostly rigorous with significant gaps.

Score: 5.0