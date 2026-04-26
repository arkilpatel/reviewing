### Claimed Contributions
1. Proves that privacy amplification by synthetic data release persists even when releasing an unbounded number of synthetic records ($n_{\text{syn}} \to \infty$), under a bounded-parameter assumption for a linear generator.
2. Derives new technical tools bounding the Fisher information for non-central chi-squared and non-central Wishart distributions.
3. Establishes a local relationship criterion to control Rényi divergences via Fisher information, correcting flaws in prior literature.
4. Provides numerical estimations using variational inference that confirm the theoretical convergence and tightness of the bounds.

### Prior Work Assessment
- Differential privacy for synthetic data is a critical area. Recently, Pierquin et al. (2025) established the first formal amplification guarantees for a linear generator. However, their proofs required the restrictive assumption that the number of synthetic records is much smaller than the model dimension ($n_{\text{syn}} \ll d$), and their bounds were piecewise.
- The authors directly tackle and dismantle this limitation, showing that the amplification is not merely an artifact of small sample sizes but an intrinsic property of the latent randomness in the generation process, bounded by the parameter norm.

### Novelty Verdict
Substantial

### Justification
The paper provides a surprising and highly significant theoretical result that overturns a recently established limitation in the DP literature. The shift from analyzing the finite $n_{\text{syn}}$ trade-off to utilizing the sufficient statistics of Gram matrices ($V^T V$) in the infinite limit is a mathematically elegant and novel approach. Furthermore, the introduction of new Fisher information bounds for non-central Wishart distributions is a strong contribution to mathematical statistics in its own right.

Score: 8.0