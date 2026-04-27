### Claimed Contributions
1. dXPP, a penalty-based approach to differentiating through black-box QP solvers that supposedly bypasses KKT differentiation and reduces the backward pass to a primal-dimensional SPD linear system.
2. Theoretical proof that the sensitivity computed from the smoothed penalty objective converges to the exact KKT sensitivity as the smoothing parameter tends to zero.
3. Empirical evaluation showing state-of-the-art scalability for differentiating QPs on various benchmarks.

### Prior Work Assessment
The paper claims to bypass KKT differentiation by using a smoothed penalty formulation. However, a careful mathematical analysis reveals that their proposed method is analytically identical to a well-known trick: solving the KKT system by adding Tikhonov regularization to the dual variables and reducing the system via the Schur complement. 
Specifically, regularizing the dual variables of the KKT system with a negative diagonal block $-\delta W^{-1}$ and taking the Schur complement of the (2,2) block yields exactly the coefficient matrix $P + \frac{1}{\delta} B^T W B$ derived in Eq (13) of the paper. 
Therefore, the "smoothed exact penalty" framing is essentially a theoretical wrapper around the Schur complement reduction of a regularized KKT system. While the connection between penalty methods and dual-regularized KKT systems is known in optimization (e.g., in ALM and interior point methods), framing this as a fundamentally novel alternative that "bypasses" KKT is somewhat misleading. The true novelty lies in applying this specific Schur complement reduction to differentiable optimization layers to improve backward pass scalability, rather than inventing a non-KKT differentiation mechanism.

### Novelty Verdict
Moderate

### Justification
The practical contribution—reducing the indefinite KKT system to a smaller, SPD primal system for backpropagation—is highly useful and addresses a real scalability bottleneck in differentiable optimization. However, the theoretical framing overclaims the novelty of the mechanism. It is a creative and effective application of classical Schur complement reduction and regularization, but not a fundamentally new paradigm of differentiation.

### Missing References
The paper should explicitly discuss the equivalence of their penalty formulation's Hessian to the Schur complement of a dual-regularized KKT system, citing standard texts on numerical optimization (e.g., Nocedal & Wright) regarding this equivalence.
