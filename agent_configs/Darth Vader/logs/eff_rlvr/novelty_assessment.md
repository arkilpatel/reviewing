### Claimed Contributions
1. Identifying that difficulty-based data selection heuristics in RLVR (which select data with success rates near 0.5) conflate aleatoric and epistemic uncertainty, thereby ignoring the accumulated evidence of previous rollouts.
2. Introducing INSIGHT, a data selection method that uses a Weighted Mutual Information (WMI) objective, explicitly decoupling epistemic uncertainty (measured by Mutual Information) from task difficulty (measured by a heuristic weighting function on the expected success rate).
3. Analytically extending the Mutual Information objective to the multi-rollout setting (K rollouts per prompt) common in GRPO-style RLVR.

### Prior Work Assessment
- **Prior Work:** MOPPS (Qu et al., 2025) and BOTS (Shen et al., 2025a) frame RLVR data selection as a multi-armed bandit problem, modeling success rates with Beta-Bernoulli distributions. MOPPS selects tasks near a target difficulty using Thompson sampling (sampled success rates). 
- **Delta:** The paper correctly points out that sampled success rates conflate epistemic and aleatoric uncertainty. However, the proposed solution—using expected information gain (Mutual Information) combined with a difficulty preference—is practically a textbook application of Bayesian active learning and Bayesian optimization acquisition functions (e.g., expected error reduction, BALD). The novelty lies entirely in applying these well-established statistical principles to correct a recent heuristic in the highly specific, newly emerging sub-field of RLVR data selection. 

### Novelty Verdict
Incremental

### Justification
The application of Mutual Information to model epistemic uncertainty, coupled with a weighting function for task difficulty, is a standard technique in Bayesian experimental design. The paper does not invent a new statistical framework; rather, it takes established active learning methods and ports them to the context of LLM reinforcement learning to fix a theoretical looseness in concurrent work (MOPPS). While the analytical extension to the multi-rollout setting (Equation 13) is a nice touch, the overall conceptual delta is predictable for anyone familiar with Bayesian active learning.

### Missing References
The paper could benefit from citing foundational Bayesian active learning and experimental design literature (e.g., Houlsby et al., "Bayesian Active Learning for Classification and Preference Learning" or MacKay's work on information-based objective functions) to better contextualize where the WMI formulation originates, rather than presenting it purely as a novel derivation for LLMs.

**Score: 4.5/10**
