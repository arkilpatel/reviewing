### Claimed Contributions
1. Proposes "Retrieve and Play" (R&P), a simple 1-nearest-neighbor baseline for sequential decision making that acts as a strong adaptation mechanism.
2. Proposes REGENT, a semi-parametric architecture that pre-trains a transformer policy on sequences of queries and retrieved context (state, reward, action).
3. Demonstrates that REGENT can generalize to unseen environments via in-context learning without fine-tuning, using significantly fewer parameters and data than state-of-the-art generalist agents like Gato and MTT.

### Prior Work Assessment
- Methodological Novelty: The idea of using retrieval-augmentation in reinforcement learning has been explored recently (e.g., Retrieval-Augmented Decision Transformer [39], Retrieval-augmented embodied agents [61]). However, REGENT specifically focuses on interpolating between a 1-NN R&P baseline and a transformer policy using an exponential distance weighting scheme to enable zero-shot in-context adaptation to unseen environments. The interpolation scheme (Eq 1) is a neat adaptation of distance-weighted residual prediction.
- Empirical/Insight Novelty: Showing that a simple 1-NN R&P agent is a surprisingly strong baseline for generalist agents is an insightful empirical finding. It challenges the prevailing narrative that simply scaling model size and pre-training data is the only path forward.

### Novelty Verdict
Substantial

### Justification
While retrieval-augmentation in RL is not fundamentally new, the specific instantiation in REGENT—particularly the distance-weighted interpolation with the R&P baseline—and its application to zero-shot adaptation in entirely unseen environments represents a substantial step forward. The empirical insight regarding the strength of the 1-NN baseline is also highly valuable to the community. The delta over prior work like MTT (Multi-Trajectory Transformer) is clear in both methodology and efficiency.

### Missing References
None apparent. The related work adequately covers recent generalist agents (Gato, RT-1, RoboCat, MTT) and retrieval-augmented language models.
