### Claims Inventory
1. **Theoretical:** Expected variance reduction of a Beta posterior decays rapidly with accumulated evidence (n), revealing a limitation of purely difficulty-based heuristics.
2. **Theoretical:** Mutual Information correctly captures epistemic uncertainty in the Beta-Bernoulli model and scales asymptotically as $O(1/n)$.
3. **Empirical:** The WMI objective (INSIGHT) improves training efficiency and final reasoning performance compared to uniform sampling and difficulty-only heuristics.

### Verification Results
1. **Variance reduction derivation:** Verified. Equation 8 correctly derives that the expected variance reduction of a Beta-Bernoulli model after 1 observation is exactly proportional to $1/(n+1)^2$.
2. **Mutual Information derivation:** Verified. Equation 13 correctly computes the mutual information for $K$ independent rollouts using the Beta-Binomial predictive distribution. Proposition 5.1 correctly applies a Gaussian approximation to show that MI decays as $O(1/n)$.
3. **WMI formulation:** Concern. The authors multiply Mutual Information (a rigorous information-theoretic quantity) by an ad-hoc weighting function $w(\bar{\phi})$ that manually biases towards high variance and a target difficulty $\mu$. This multiplicative combination is heuristic and lacks a rigorous information-theoretic justification, though it is a common practical approximation in applied active learning.

### Errors and Concerns
- **Minor Concern (Heuristic Weighting):** The weighting function $w(\bar{\phi})$ relies on a hand-crafted exponential decay centered around $\mu$ combined with a variance filter. This makes the acquisition function heavily dependent on hyperparameters ($\eta$, $\mu$) and detracts from the "principled" nature of the information-theoretic claims.
- **Theory-Practice Gap (Non-stationarity):** The theoretical derivations assume a stationary latent success rate $\phi_\tau$. However, in RL, the policy is constantly updating, meaning $\phi_\tau$ is non-stationary. The paper handles this practically using a simple exponential moving average decay ($\lambda$) on the Beta counts (Equation 6). The Beta-Bernoulli model with count decay is a crude approximation of this non-stationarity, and the paper does not theoretically analyze the lag or tracking error this introduces into the Mutual Information estimates.

### Internal Consistency Check
The mathematical derivations are consistent with the algorithmic implementation described in Algorithm 1. The transition from theoretical single-rollout variance reduction to multi-rollout Mutual Information is well-motivated and consistent.

### Theory-Practice Gap Assessment
As noted above, the theoretical derivations of Mutual Information assume a static generative process for the rewards, whereas the experimental setting involves a dynamically changing RL policy. This gap is bridged by a heuristic count decay, which is standard but leaves the theoretical guarantees partially disconnected from the empirical reality.

### Overall Technical Soundness Verdict
Sound with minor issues

**Score: 7.5/10**
