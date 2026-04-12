# Synthesized Review: Attention as a Compass

## Overview
The paper presents AttnRL, a novel framework for Process-Supervised Reinforcement Learning (PSRL) in reasoning models. The authors propose using Forward Context Influence (FCI) scores—derived from the model's internal attention mechanisms—to identify critical reasoning steps and branch from them during Monte Carlo sampling. This replaces the naive entropy-based branching seen in prior work (e.g., TreeRL). Furthermore, the paper introduces an adaptive sampling strategy to bias tree expansion towards harder problems and ensure batches contain non-zero advantage tokens. Finally, they engineer a one-step off-policy training pipeline that halves the generation overhead per training iteration. The method outperforms strong baselines like GRPO and TreeRL across multiple math reasoning benchmarks.

## Strengths
1. **Bridging Interpretability and RL:** Using attention spikes (FCI) as a proxy for reasoning importance to guide the RL search tree is an elegant, empirically validated idea that effectively replaces ad-hoc entropy heuristics.
2. **Computational Efficiency:** PSRL's main bottleneck is its extreme sampling cost. The combination of targeted branching, dropping 100%-correct initial samples, and the one-step off-policy pipeline is a highly practical engineering contribution that makes process supervision scalable.
3. **Consistent Empirical Gains:** The method demonstrates consistent improvements over strong recent baselines (GRPO, TreeRL) across six challenging mathematical benchmarks and two different model sizes (1.5B and 7B).
4. **Strong Ablations:** The ablation study successfully isolates the benefits of Attention-based Tree Branching (ATB) and Adaptive Sampling (ADS).

## Weaknesses
1. **Lack of Variance Reporting:** The main results table lacks standard deviations or variance across multiple random seeds, which is a common but persistent flaw in RL papers. 
2. **Heuristic Dependencies:** Certain components rely on fixed, somewhat arbitrary heuristics (e.g., the $\rho=0.2$ quantile for FCI thresholding, exponential decay for tree expansion). The paper would benefit from a sensitivity analysis on these parameters.

## Conclusion
This is a high-quality paper with substantial practical impact. It directly addresses the scaling bottlenecks of Reinforcement Learning with Verifiable Rewards (RLVR) by making process supervision more computationally tractable and exploration more targeted. The methodology is sound, and the results are consistent.

## Scoring Breakdown
- **Impact (40%):** 8.0 / 10.0
- **Technical Soundness (20%):** 9.0 / 10.0
- **Experimental Rigor (20%):** 8.0 / 10.0
- **Novelty (20%):** 8.0 / 10.0

**Formula applied:** Standard (Empirical) -> `(4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 8.20