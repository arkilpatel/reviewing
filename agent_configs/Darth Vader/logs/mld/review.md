## Final Review

This paper investigates the theoretical properties of mini-batch gradient noise in microcanonical dynamics, identifying an anisotropic drift that causes the stationary distribution to deviate from the true posterior. To resolve this, the authors introduce pSMILE, applying gradient preconditioning as a requirement for stationarity in non-dissipative microcanonical Langevin dynamics. An energy-variance adaptive tuner using a Gamma distribution is also proposed. 

While the theoretical diagnosis of anisotropic noise-induced drift and the conceptual framing of preconditioning as a stationarity requirement are highly novel and significant, severe technical and experimental flaws undermine the paper in its current state.

### Novelty
The paper identifies a fundamental tension between mini-batch noise and the geometric constraints of microcanonical MCMC. While preconditioning itself is an existing tool in the MCMC literature, applying it to correct the anisotropic noise-induced drift in Hamiltonian-conserving dynamics is a novel, principled use case. The theoretical framing elevates the novelty beyond a simple empirical combination of MILE and Adam-style preconditioning. The core mechanism of fluctuation without dissipation in microcanonical dynamics was established previously (Jakob et al., 2024; MILE). The novelty here lies in diagnosing why naive mini-batching fails (anisotropic drift) and formulating preconditioning as the solution.

### Technical Soundness
There are fundamental flaws in the technical execution:
1. **Algebraic Error in Gamma Parameterization:** Equation 5 contains a fundamental error in the moment-matching formulas for the online Gamma distribution fitting. The manuscript assigns $\gamma_{\text{shape}} = \sigma^2/\mu$ and $\gamma_{\text{scale}} = (\mu/\sigma)^2$. In standard probability theory, for a Gamma distribution with mean $\mu$ and variance $\sigma^2$, the scale is $\sigma^2/\mu$ and the shape is $\mu^2/\sigma^2$. The labels in the manuscript are reversed. This mathematical error directly affects the Wilson-Hilferty transform used for the adaptive step-size guardrails, undermining the algorithmic reliability of the tuner.
2. **Unquantified Riemannian Bias:** The preconditioning matrix $\mathbf{L}(\boldsymbol{\theta})$ is treated as locally constant to avoid computing its divergence. By omitting this required Riemannian correction term, the continuous-time dynamics do not strictly preserve the target posterior. The paper fails to quantify the magnitude of this bias or prove that it is negligible compared to the anisotropic noise bias it aims to correct.
3. **Stationary Distribution Guarantee:** The paper does not theoretically characterize the deviation of the stationary distribution from the true posterior under mini-batch gradient noise. While preconditioning corrects anisotropic scaling, stochastic sub-sampling still introduces bias that the Hamiltonian projection does not inherently fix.
4. **SDE Singularity:** The momentum update (Equation 2) contains a scaling factor of $(d-1)^{-1}$, which is singular for $d=1$. The theoretical domain ($d \ge 2$) must be explicitly defined for mathematical completeness.

### Experimental Rigor
The empirical evaluation is highly problematic:
1. **Compute-Confounded "State-of-the-Art" Claims:** The headline empirical results on CIFAR-100/ResNet-18 (Table 2) achieve "state-of-the-art" accuracy by using an 8-member ensemble (pSMILE-8), whereas the baseline methods (like cSGLD) are evaluated as single chains. Ensembling naturally improves predictive performance and uncertainty calibration. Without normalizing for Total Gradient Evaluations (TGE) or wall-clock compute, it is impossible to separate the algorithmic gains of microcanonical dynamics from the brute-force benefit of running 8 chains.
2. **Missing Essential Baseline:** The core algorithmic contribution is preconditioning in a stochastic gradient MCMC context. Yet, pSGLD (Li et al., 2016)—the canonical preconditioned SGMCMC method—is entirely absent from the empirical comparisons. Comparing against non-preconditioned baselines (SGHMC, cSGLD) artificially inflates the apparent advantage of pSMILE.
3. **Efficiency Metrics:** The paper claims scalability but evaluates primarily on downstream accuracy rather than canonical MCMC efficiency metrics. Effective Sample Size (ESS) per gradient evaluation or ESS per second is not reported for the Bayesian Neural Network tasks, making the efficiency claims difficult to verify formally.

### Impact
Scaling exact or near-exact Bayesian inference to the size of deep neural networks remains an open, high-value problem. Bridging the gap between the geometric advantages of microcanonical dynamics and the necessity of mini-batch stochastic gradients is a highly significant research direction. The insight that preconditioning is a necessary stationarity requirement to counteract anisotropic noise drift is scientifically impactful and likely to influence future design of stochastic samplers. However, the technical and empirical execution limits the immediate real-world adoption of pSMILE. The algebraic errors and the lack of compute-normalized comparisons imply that practitioners cannot yet trust that the performance gains justify the implementation complexity over simpler baselines. 

### Scoring Breakdown
- **Impact:** 6.0
- **Technical Soundness:** 3.0
- **Experimental Rigor:** 3.0
- **Novelty:** 7.0

**Formula applied:** (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10
**Final Score:** 5.0
