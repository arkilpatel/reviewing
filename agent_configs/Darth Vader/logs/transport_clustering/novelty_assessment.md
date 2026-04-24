### Claimed Contributions
1. Reducing the non-convex, NP-hard low-rank optimal transport (LR-OT) problem to a simpler clustering problem on correspondences (called "transport clustering").
2. Proving that this reduction (using the full-rank Monge or Kantorovich plan to register the cost) yields polynomial-time, constant-factor approximation algorithms for LR-OT, specifically (1+gamma) for negative-type metrics and (1+gamma+sqrt(2gamma)) for kernel costs.
3. Introducing a specific algorithm (TC) using mirror descent and generalized K-means, and demonstrating empirically that it outperforms existing LR-OT methods (like LOT, FRLC, LatentOT) on synthetic benchmarks and large-scale single-cell transcriptomics.

### Prior Work Assessment
- Existing LR-OT methods: LOT (Scetbon et al. 2021) and FRLC (Halmos et al. 2024) optimize a complex non-convex objective over multiple variables, which can be sensitive to initialization and only guarantee convergence to stationary points.
- The connection between LR-OT and generalized K-means was established by Scetbon & Cuturi (2022). However, their reduction only worked when the datasets are the same ($X=Y$).
- The delta here is utilizing the full-rank transport plan (Monge map or Kantorovich plan) to "register" the cost matrix across different datasets $X$ and $Y$, thus extending the reduction to the co-clustering case and achieving provable approximation guarantees.

### Novelty Verdict
Substantial

### Justification
The paper establishes a clever and previously unrecognized algorithmic reduction. While Scetbon & Cuturi (2022) noted the connection between LR-OT and K-means, it was restricted to single datasets. Using full-rank OT as a pre-processing "registration" step to enable K-means across two datasets is conceptually elegant. Proving constant-factor approximation guarantees for this reduction is a significant theoretical advance for a problem that is known to be NP-hard and practically tricky to optimize. The empirical validation on massive scale datasets further confirms the novelty and practical utility of this approach. It is a substantial step over existing iterative alternating-minimization solvers.

### Missing References
None apparent. The authors extensively cite recent work on LR-OT, including LOT, FRLC, and related methods.
