# Review: Hard labels sampled from sparse targets mislead rotation invariant algorithms

## Overview
This paper investigates the behavior of rotation-invariant learning algorithms (e.g., standard gradient descent on linear layers) versus non-rotation-invariant algorithms (e.g., gradient descent on spindly $u \odot v$ reparameterized layers) in the context of over-constrained sparse logistic regression. The authors demonstrate that when learning from sampled hard labels, rotation-invariant algorithms are provably suboptimal, whereas non-rotation-invariant algorithms can efficiently recover the sparse targets.

### Novelty
The theoretical formulation that hard labels (as opposed to soft conditional probabilities) break the capability of rotation-invariant algorithms in the over-constrained regime without additive noise is highly novel. While similar failures were known for square loss with noise, isolating this phenomenon for logistic loss under hard-label sampling is a subtle and important observation. The methodology, particularly solving the state-dependent Riccati-type ODEs for the logistic link, is a fresh theoretical contribution.

### Technical Soundness
The paper is mathematically rigorous. The authors successfully establish a lower bound (Theorem 3.5) proving an excess risk of $\Omega(d/n)$ for any rotation-invariant algorithm, contrasting it with an upper bound (Theorem 5.1) of $O(s \log(d) / n)$ for the non-rotation-invariant spindly model. The proof techniques—ranging from analyzing posterior concentration on a sphere to ODE enveloping arguments—are robust, well-motivated, and fully support the main claims under the standard isotropic Gaussian design assumption.

### Experimental Rigor
The experimental validation focuses on synthetic datasets ($d=50, s=5, n=1000$) to verify the theoretically derived scaling laws. The plots clearly corroborate the gap in excess risk scaling between the two parameterizations. While appropriate for a foundational theory paper, the empirical section would be much stronger if it included experiments on real-world sparse datasets or explored the implications in deeper architectures to bridge the gap between theory and practice.

### Impact
Given that logistic modeling is ubiquitous as the final layer in deep neural networks, this work carries significant implications. The mathematical proof that hard labels inherently obstruct sparse target recovery for standard architectures provides theoretical grounding for why soft-label techniques (like distillation) are so effective. It also suggests actionable architectural modifications (spindly parameterization) to improve sample efficiency in sparse settings, promising high impact in both theoretical and applied ML.

---

### Scoring Breakdown
- **Novelty:** 8.0
- **Technical Soundness:** 8.5
- **Experimental Rigor:** 6.5
- **Impact:** 7.5

**Formula applied:** Theory Papers
`score = (3.0 * Impact + 3.0 * Tech_Soundness + 2.0 * Novelty + 2.0 * Exp_Rigor) / 10`

**Calculation:**
`score = (3.0 * 7.5 + 3.0 * 8.5 + 2.0 * 8.0 + 2.0 * 6.5) / 10`
`score = (22.5 + 25.5 + 16.0 + 13.0) / 10`
`score = 77.0 / 10 = 7.7`

**Final Score:** 7.7
