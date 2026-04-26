# Comprehensive Review of "Privacy Amplification Persists under Unlimited Synthetic Data Release"

## Summary
This paper investigates the phenomenon of privacy amplification through synthetic data release. While it is known that releasing synthetic data from a differentially private (DP) model inherits the model's privacy guarantees via post-processing, empirical evidence suggests the actual leakage is often much lower. Prior theoretical work (Pierquin et al., 2025) proved this amplification effect for a linear generator but required a highly restrictive assumption that the number of synthetic records ($n_{\text{syn}}$) is vastly smaller than the model dimension $d$. This paper definitively overturns that limitation, proving that under a bounded-parameter assumption, privacy amplification persists even as $n_{\text{syn}} \to \infty$. To achieve this, the authors develop new Fisher information bounds for non-central Wishart distributions and provide numerical estimates via variational inference to confirm the theory.

## Novelty
The paper provides a surprising and highly significant theoretical result that challenges a recently established limitation in the DP literature. The analytical shift from studying the finite $n_{\text{syn}}$ trade-off to utilizing the sufficient statistics of Gram matrices ($V^T V$) in the infinite limit is mathematically elegant. Furthermore, deriving new Fisher information bounds for non-central Wishart distributions represents a strong and independent contribution to mathematical statistics.

## Technical Soundness
The mathematical foundation of the paper is exceptionally strong. The reduction of the infinite data release problem to the distinguishability of Gram matrices is rigorously justified. The authors cleverly navigate the intractability of the generalized hypergeometric function of a matrix argument (${}_0F_1$) by constructing a smooth path and applying orthogonal transformations to bound the Fisher information. A highly commendable aspect of the paper is its rigorous treatment of the relationship between Fisher information and Rényi divergences. The authors explicitly construct a counterexample to false claims in prior literature (Abbasnejad 2006, Habibi 2006) regarding pointwise ordering of Fisher information implying the ordering of Rényi/KL divergences. This level of mathematical hygiene is superb.

## Experimental Rigor
Because the densities of the non-central Wishart distributions are analytically intractable for computing divergences, the authors employ the Convex-Conjugate Rényi Variational Formula (Birrell et al., 2023) using a neural network optimized via stochastic gradient ascent. The experiments precisely target and validate the theoretical claims: they empirically confirm that the Rényi divergence rapidly plateaus as $n_{\text{syn}}$ increases (confirming the $n_{\text{syn}} \to \infty$ theorem) and validate the tightness of the local bounds. For a heavily theoretical paper, the numerical simulations are completely appropriate and sufficient.

## Impact
Understanding the exact privacy loss incurred by synthetic data release is a fundamental open problem in DP. This paper makes a definitive contribution to the foundational theory. While the analysis is currently restricted to a tractable linear generator with output perturbation, the structural insights lay a solid mathematical groundwork for extending these proofs to more complex mechanisms like Noisy Gradient Descent or non-linear generators. For the theoretical DP community, this paper will likely be highly influential.

## Scoring Breakdown
- **Impact:** 7.0
- **Technical Soundness:** 9.0
- **Experimental Rigor:** 7.0
- **Novelty:** 8.0

**Formula applied:** (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10
**Final Score:** 7.6