### Claimed Contributions
1. A post-training KV-cache compression method (StiefKV) that learns orthonormal projection bases by directly minimizing the full decoder-layer output reconstruction error, rather than intermediate proxy objectives.
2. A lightweight MLP-based predictor that generates these bases from simple activation statistics (mean and variance of keys and values) via QR decomposition.
3. A precomputed layer-wise error-rank profile that enables flexible, depth-adaptive rank allocation under a user-specified error budget without requiring retraining.
4. Empirical demonstration on Llama3-8B showing substantial improvements over EigenAttention at matched KV-cache budgets (e.g., +5.4% MMLU, -11.9 C4 perplexity).

### Prior Work Assessment
- KV cache compression via low-rank decomposition is an active area. Existing state-of-the-art methods like EigenAttention apply SVD-style optimizations directly to the Key/Value matrices or the intermediate attention output.
- The fundamental critique offered by this paper—that proxy SVD objectives fail to model the non-linear interactions of softmax, value mixing, and subsequent MLP/residual blocks—is accurate and well-placed.
- Learning orthogonal bases (Stiefel manifold) via differentiable QR decomposition is an established technique in deep learning, but its specific application as a conditioned basis predictor for post-training KV compression is a fresh synthesis.

### Novelty Verdict
Substantial

### Justification
While the individual components (QR decomposition for orthogonality, Pareto optimization for rank allocation) are standard, applying them to directly minimize the decoder-layer output error for KV compression is a novel and highly effective architectural choice. The shift from static SVD factorization to a trained, statistics-conditioned MLP predictor that optimizes end-to-end layer fidelity represents a meaningful conceptual advance over prior proxy-objective methods.

Score: 7.0