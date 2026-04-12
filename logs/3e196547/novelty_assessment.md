### Claimed Contributions
1. **Attention-based Tree Branching (ATB):** A novel branching strategy for Monte Carlo sampling in PSRL, which uses the Forward Context Influence (FCI) scores derived from attention weights to select reasoning-critical steps as branching points, rather than using token entropy.
2. **Adaptive Sampling Mechanism:** A method that filters out overly easy problems (using average FCI as a proxy) and dynamically allocates more tree expansions to harder problems, while also adaptively sizing the prompt batch to guarantee that the final training batch contains only non-zero advantage tokens.
3. **One-Step Off-Policy Training:** An efficient training pipeline that interleaves the initial sampling of the next batch with the MC sampling of the current batch, effectively reducing the number of generation phases per training iteration from two to one.

### Prior Work Assessment
- **TreeRL (Hou et al. 2025):** Introduces tree-based advantage estimation and MC branching for PSRL. However, it relies on simple entropy-based branching and uniform sampling across problems. AttnRL directly builds on TreeRL but replaces the naive heuristics with computationally grounded ones (attention).
- **Massive Attention in LLMs (Bogdan et al. 2025, Jin et al. 2025):** These interpretability works showed that attention spikes correlate with contextual importance and specific reasoning behaviors (e.g., self-verification). AttnRL novelly applies this interpretability finding as an active heuristic for RL search tree expansion.
- **Delta:** The delta is substantial. While tree-based PSRL is an existing paradigm, effectively steering the search tree using the model's internal attention mechanisms is a fresh, insightful approach that bridges interpretability and RL. The addition of the one-step off-policy training pipeline also provides a non-trivial engineering contribution that makes PSRL vastly more tractable.

### Novelty Verdict
Substantial

### Justification
The paper successfully merges insights from LLM interpretability (attention analysis) with the computational challenges of PSRL. Replacing entropy with FCI for branching is a principled, empirically validated improvement that clearly distinguishes itself from the uniform or entropy-driven approaches of prior work. The combination of ATB, difficulty-aware adaptive sampling, and the one-step pipeline constitutes a significant methodological and practical advance in RLVR.

### Missing References
None apparent. The authors adequately cite very recent concurrent/pre-print works (e.g., TreeRL from 2025, DeepScaleR from 2025).