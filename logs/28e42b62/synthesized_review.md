# Comprehensive Review of "GTPO AND GRPO-S"

## Overview
This paper proposes Dynamic Entropy Weighting to solve the coarse-grained credit assignment bottleneck in value-function-free Reinforcement Learning algorithms like GRPO. The authors introduce GTPO and GRPO-S, which actively reshape the reward signal using token-level and sequence-level entropy, dynamically incentivizing exploration in successful paths and penalizing confident errors in unsuccessful ones.

While the conceptual framing of using entropy as an active reward shaping mechanism is moderately novel, the execution of the paper is fundamentally broken. Severe internal contradictions invalidate both the theoretical claims and the empirical results.

## Technical Soundness
**Significant Concerns.** The theoretical foundation of the paper is contradictory. In Theorem 2.4, the authors claim that GTPO shares the same global optimum as DAPO. This proof hinges entirely on the "Entropy Consolidation Condition," which assumes that token entropy diminishes as training progresses ($k \to \infty$). However, the proposed method explicitly modifies the reward signal to *reward* high entropy in successful sequences. The PPO objective will therefore explicitly optimize the policy to increase (or at least maintain) high entropy to maximize return. The reward shaping mechanism actively opposes the assumption needed to prove it works.

## Experimental Rigor
**Critical Gaps.** The primary results in Table 1 are severely mangled, and the experimental claims contradict the provided data.
1. The text claims: *"regarding the Pass@32 metric on AIME 2024, GTPO achieves a massive absolute performance gain (APG) of +29.4 points on the 7B model, compared to +9.9 points on the 32B model"*.
2. However, looking at the layout of Table 1, the +29.4 gain is found in the second block of results, while the +9.9 gain is found in the third block (which is labeled `Qwen2.5-32B`). The first block, labeled `Qwen2.5-7B`, shows Pass@32 scores in the 78-85 range, contradicting the scaling laws of the models (where 32B should strongly outperform 7B). It appears the table blocks were mislabeled or the results were incorrectly generated/pasted, making it impossible to evaluate the true empirical performance.
3. No variance reporting or multiple random seeds are used, which is unacceptable for RL algorithms.

## Novelty
**Moderate.** Using continuous entropy-based reward scaling instead of binary filtering (like DAPO w/ Forking Tokens) is a sensible, logical extension of current value-free RL paradigms.

## Impact
**Low.** The theoretical flaws and completely unreliable empirical results mean that, despite the importance of the problem being solved, the proposed method as presented is unusable.

## Adversarial Robustness & Negligence
**Critical Concern.** The paper suffers from severe internal contradictions that trigger the Negligence Penalty.
- As noted above, the empirical results in the text directly contradict the labeling and values in Table 1.
- The theoretical section relies on the assumption that entropy will strictly decrease (Entropy Consolidation Condition), yet Section 3.3 and Figure 6 proudly point to the "Entropy Rebound" phenomenon—the explicit observation that their method causes entropy to *increase*—as the mechanism for success. This is a severe internal contradiction: the paper relies on an assumption to prove its theorem, and then relies on the failure of that exact assumption to claim empirical success.

---

## Scoring Breakdown
- **Impact (40%):** 2.0 / 10
- **Technical Soundness (20%):** 3.0 / 10
- **Experimental Rigor (20%):** 2.0 / 10
- **Novelty (20%):** 5.0 / 10

**Base Score:** `(4.0 * 2.0 + 2.0 * 3.0 + 2.0 * 2.0 + 2.0 * 5.0) / 10 = 2.8`
**Negligence Penalty Applied:** Yes (Mangled Tables and Severe Internal Contradictions). Score is halved.
**Final Score:** 1.4