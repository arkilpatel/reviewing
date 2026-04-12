### Claims-to-Experiments Mapping
- **Claim:** ATB is superior to entropy-based branching. -> Supported by Table 2 (ablation) and Figure 6 (sampling statistics).
- **Claim:** AttnRL improves final reasoning performance over baselines. -> Supported by Table 1 across 6 benchmarks.
- **Claim:** AttnRL is more efficient to train. -> Supported by Table 3 (training steps, wall-clock time) and Figure 8.

### Baseline Assessment
Baselines are appropriate, highly relevant, and strong. The authors compare against GRPO (the standard outcome-based method used in DeepSeekMath/R1) and TreeRL (the most direct prior PSRL method). They also compare against DeepScaleR-Preview-1.5B, which is a very strong current RLVR checkpoint. The baselines appear to be given fair computational treatment.

### Dataset Assessment
The paper uses AIME24, AIME25, AMC23, MATH-500, Minerva, and OlympiadBench. These are the gold-standard datasets for evaluating reasoning capabilities in LLMs currently. They are sufficiently challenging (e.g., AIME25 base accuracy is around 23%). Contamination is always a risk with public benchmarks, but the comparative nature of the RL training (all methods starting from the same base model) isolates the effect of the RL algorithm.

### Metric Assessment
Pass@1 and Pass@K (K=32 for AMC/AIME, K=4 for others) are standard and perfectly appropriate for evaluating mathematical reasoning.

### Statistical Rigor
- **Variance reporting:** The paper does not report standard deviations or variance across multiple random seeds for the main results in Table 1. This is a common flaw in LLM RL papers due to compute constraints, but it remains a gap.
- However, the risk of cherry-picking or statistical noise is mitigated by the fact that the proposed method consistently outperforms baselines across *six different datasets* and *two different model scales* (1.5B and 7B). The gains are modest but consistent.

### Ablation Assessment
Table 2 provides a solid ablation study isolating the ATB component and the Adaptive Sampling (ADS) component. It successfully demonstrates that both contribute to the final performance, and properly highlights the specific impact of the attention-based filtering.

### Missing Experiments
An experiment showing the sensitivity to the hyperparameter $\rho$ (the 20% quantile for selecting FCI steps) or the choice of $N=2$ branching points would have been welcome to understand the robustness of the heuristics.

### Error Analysis Assessment
The paper analyzes the effect of disruption at different sequence positions (Figure 3b) and visualizes the steps identified by the FCI metric (Figure 2), which provides good qualitative insight into *why* the method works.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps (primarily the lack of multi-seed variance reporting).