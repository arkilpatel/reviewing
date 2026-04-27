### Experimental Rigor Assessment

1. **Compute-Confounded "State-of-the-Art" Claims:** The headline empirical results on CIFAR-100/ResNet-18 (Table 2) achieve "state-of-the-art" accuracy by using an 8-member ensemble (pSMILE-8), whereas the baseline methods (like cSGLD) are evaluated as single chains. Ensembling naturally improves predictive performance and uncertainty calibration. Without normalizing for Total Gradient Evaluations (TGE) or wall-clock compute, it is impossible to separate the algorithmic gains of microcanonical dynamics from the brute-force benefit of running 8 chains.
2. **Missing Essential Baseline:** The core algorithmic contribution is preconditioning in a stochastic gradient MCMC context. Yet, pSGLD (Li et al., 2016)—the canonical preconditioned SGMCMC method—is entirely absent from the empirical comparisons. Comparing against non-preconditioned baselines (SGHMC, cSGLD) artificially inflates the apparent advantage of pSMILE.
3. **Efficiency Metrics:** The paper claims scalability but evaluates primarily on downstream accuracy rather than canonical MCMC efficiency metrics. Effective Sample Size (ESS) per gradient evaluation or ESS per second is not reported for the Bayesian Neural Network tasks, making the efficiency claims difficult to verify formally.
4. **Bibliography Hygiene:** The `refs.bib` file contains massive duplication (e.g., the same paper cited three times) and relies heavily on arXiv preprints for papers that have been formally published in major venues (NeurIPS, ICML).

Score: 3.0
