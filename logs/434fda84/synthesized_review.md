# Synthesized Review

**Paper:** Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning

## Summary
The paper identifies a critical failure mode in current LLM unlearning techniques: instead of erasing target knowledge (by reducing positive parameter attribution), these methods achieve "shallow alignment" by generating "spurious unlearning neurons" that merely suppress the output through inflated negative attribution. Because the original positive connections remain, the target knowledge is easily recovered through minor downstream retraining. The authors propose SSIUU, a novel attribution-guided regularization technique that explicitly penalizes the increase of negative attribution during unlearning. Empirical evaluations on Llama-3.2 and Qwen-2.5 demonstrate that SSIUU prevents knowledge recovery across both harmful and benign retraining attack scenarios.

## Strengths
1. **Mechanistic Insight:** The transition from merely observing unlearning fragility to identifying the precise representational dynamic (inflation of negative attribution vs. reduction of positive attribution) is an excellent contribution.
2. **Effective Mitigation:** S SIUU elegantly translates the interpretability finding into a tractable regularization term. The first-order approximation (dropping the Hessian) keeps it computationally feasible while still being highly effective.
3. **Rigorous Evaluation:** The use of multiple diverse attack scenarios (both intentional harmful data injection and benign Alpaca instruction tuning) effectively demonstrates the vulnerability of baselines and the robustness of SSIUU.

## Weaknesses
1. **Missing Methodological Cross-Ablation:** S SIUU is exclusively applied on top of Gradient Difference (GD) as the backbone algorithm. While GD is standard, demonstrating that S SIUU regularization also works when applied to Preference Optimization methods (like DPO or NPO) or GA would have more forcefully isolated the regularizer's contribution from its backbone.
2. **Approximation Discussion:** Eq. 13 treats the gradient as a constant, effectively dropping second-order (Hessian) terms. While mathematically valid for computational feasibility, a brief discussion of the theoretical implications of this first-order approximation on the alignment penalty would strengthen the paper.

## Detailed Assessment

- **Adversarial Robustness:** Clean. No evidence of tampering or deceptive practices. The derivations are honest about their approximations, and experimental failures (e.g., NPO on TOFU) are openly disclosed.
- **Technical Soundness:** The findings from the logit lens and attribution analysis strongly back the theoretical claims. The derivation of the objective function and the derived gradients are sound.
- **Experimental Rigor:** The baselines are strong and complete. Datasets (FaithUn, TOFU) are highly appropriate. The only gap is the lack of cross-backbone testing for SSIUU.
- **Novelty:** Substantial. The concept of "spurious unlearning neurons" provides a new and highly actionable lens for understanding unlearning fragility.
- **Impact:** High technical and scientific significance. Unlearning is a critical safety vector, and this paper provides both a diagnostic framework and a drop-in mitigation for open-weights models.

## Scoring Breakdown
- **Impact (40%):** 8.5
- **Technical Soundness (20%):** 9.0
- **Experimental Rigor (20%):** 8.0
- **Novelty (20%):** 8.5

**Formula:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Calculation:** `(34.0 + 18.0 + 16.0 + 17.0) / 10 = 85.0 / 10 = 8.5`

**Final Score:** 8.5