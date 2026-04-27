### Claimed Contributions
1. Identifying calibration collapse in pointwise self-verification and diversity collapse in self-aggregation methods during parallel reasoning.
2. **V1-Infer**: An uncertainty-guided pairwise self-verification algorithm that employs a Swiss-system tournament to efficiently allocate verification compute to the most uncertain candidate pairs.
3. **V1-PairRL**: An online reinforcement learning framework that jointly trains a single LLM to act as both a solution generator and a pairwise self-verifier, allowing the verifier to adapt to the generator's evolving distribution.

### Prior Work Assessment
- **Pointwise vs. Pairwise Evaluation**: The fact that pairwise comparisons are better calibrated and easier for models/humans than pointwise scoring is well-established in the reward modeling (RLHF) and LLM-as-a-judge literature (e.g., Bradley-Terry models, Zheng et al. 2023). However, applying this insight specifically to *test-time self-verification* for parallel reasoning is a relatively fresh perspective. Prior test-time scaling methods heavily rely on pointwise Outcome Reward Models (ORMs) or Process Reward Models (PRMs) (e.g., Lightman et al. 2023, Snell et al. 2024).
- **Test-time Scaling via Aggregation vs Verification**: The observation that self-aggregation (e.g., RSA by Venkatraman et al. 2025) causes diversity collapse (dropping Pass@N) is an astute empirical finding that motivates explicit verification.
- **Efficient Pairwise Ranking**: Using Swiss-system tournaments and active-learning-inspired pair selection to reduce the $O(N^2)$ complexity of pairwise comparisons is a clever combination of existing ranking algorithms applied to LLM inference.
- **Joint Training**: Prior works like "Putting Value in RL" (Sareen et al. 2025) and "Trust & Verify" (Liu et al. 2025) have explored joint training of generators and verifiers, but they focus on pointwise verification. Utilizing online RLVR (like GRPO) to dynamically generate candidate pairs for a pairwise verification loss is a conceptually elegant and novel training paradigm.

### Novelty Verdict
Substantial

### Justification
While the core components—pairwise ranking, Swiss tournaments, and RLVR—are not entirely new in isolation, their combination into a unified framework for test-time scaling is highly original. The paper successfully bridges the gap between reward modeling (where pairwise is standard) and test-time verification (where pointwise has dominated). The V1-PairRL objective, which co-evolves the generator and pairwise verifier online to avoid distribution shift, is a significant methodological advance over offline or pointwise co-training methods. The insights regarding diversity collapse in aggregation methods also add meaningful conceptual novelty.

### Missing References
The authors have cited concurrent and relevant works (RSA, GRPO, Sareen et al. 2025, Liu et al. 2025). No glaring omissions are present, though connections to active learning for ranking (e.g., Jamieson & Nowak 2011) could further contextualize the Swiss-system phase.
