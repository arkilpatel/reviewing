### Claims Inventory
- The paper claims to solve the coarse-grained credit assignment problem in GRPO.
- It claims that GTPO and GRPO-S share the same global optimum as DAPO/GRPO (Theorem 2.4).
- It claims that dynamic entropy weighting encourages exploration without shifting the optimal policy.

### Verification Results
- Global optimum claim: Error Found.
- Entropy Consolidation Condition: Error Found.

### Errors and Concerns
- **Significant Error in Theorem 2.4 (Theoretical Consistency):** The paper claims that GTPO shares the same global optimum as DAPO. The proof relies on the "Entropy Consolidation Condition," which assumes that as training progresses ($k \to \infty$), the token entropy diminishes. However, because GTPO *explicitly rewards* high-entropy tokens in successful sequences, the PPO optimization process will naturally push the policy to *increase* (or at least maintain) high entropy on those tokens to maximize the expected return. Therefore, the reward shaping creates a positive feedback loop that actively opposes the "Entropy Consolidation Condition." The assumption contradicts the optimization dynamics, invalidating the theoretical guarantee.
- **Concern (Reward Normalization):** The entropy weighting term $H_{i,t} / \sum H_{k,t}$ divides by the sum of entropies. If the policy converges toward a deterministic state (as is common in RL on math tasks), the denominator approaches zero. The paper mentions an $\epsilon$ to prevent singularity, but as entropy drops below $\epsilon$, the reward shaping becomes entirely dependent on an arbitrary hyperparameter rather than meaningful signal.

### Internal Consistency Check
- The mathematical derivation claims entropy will decrease (Consolidation Condition), while the experimental analysis (Section 3.3 and Figure 6) proudly points out an "Entropy Rebound" phenomenon where entropy explicitly increases due to the method. These two sections contradict each other.

### Overall Technical Soundness Verdict
Significant concerns. The theoretical justification for the method is fundamentally flawed due to contradictory assumptions about how the policy will react to the modified reward.