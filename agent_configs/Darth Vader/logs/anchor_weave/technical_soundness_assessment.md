### Claims Inventory
1. **Conceptual Claim**: Global 3D reconstruction from multi-view historical frames introduces accumulated cross-view misalignment (pose and depth errors) that degrade generative quality when used as a conditioning signal.
2. **Conceptual/Empirical Claim**: Per-frame local 3D point clouds inherently avoid multi-view fusion drift and provide cleaner geometric guidance.
3. **Algorithmic Claim**: The coverage-driven memory retrieval algorithm effectively selects a set of local memories that maximizes visible coverage of the target trajectory.
4. **Empirical Claim**: The multi-anchor weaving controller (pose-guided fusion + shared attention) successfully reconciles residual cross-view inconsistencies, improving rendering quality over naive fusion.
5. **Empirical Claim**: AnchorWeave outperforms state-of-the-art baselines on RealEstate10K and DL3DV in long-horizon scene consistency and visual quality.

### Verification Results
1. **Verified**: It is a well-known fact in 3D vision that fusing dense, long-horizon RGB-D frames without perfect bundle adjustment leads to noisy geometry.
2. **Verified**: Local point clouds from a single view do not suffer from cross-view fusion errors by definition, though they may still have single-view depth inaccuracies.
3. **Verified**: The greedy selection strategy described in Algorithm 1 is a standard and effective approximation for maximizing coverage (a variation of the Set Cover problem).
4. **Verified**: The ablation study explicitly demonstrates that pose-guided fusion suppresses misaligned anchors better than average fusion.
5. **Verified**: The quantitative results and visual comparisons provided support the claim that AnchorWeave achieves better consistency and fewer hallucinations than global 3D conditioning (SPMem) and other baselines.

### Errors and Concerns
- **Concern (Not Error) - Neural Weaving Capacity**: While the paper claims the weaving controller reconciles inconsistencies, this relies entirely on the neural network's ability to learn out residual misalignments. The paper does not theoretically guarantee this, but empirically demonstrates it. It would be helpful to understand the failure modes when the local depth estimates are grossly incorrect.
- **Concern (Not Error) - Memory Retrieval Overhead**: Algorithm 1 requires rendering candidate point clouds to evaluate their additional coverage. The computational overhead of this retrieve-and-render loop at every chunk could be a practical limitation, though the paper does not extensively analyze this latency.

### Internal Consistency Check
The claims align perfectly with the methodology and experiments. The problem identified (noisy global 3D) is directly addressed by the proposed solution (local 3D), and the ablation studies specifically test the components introduced to make this solution work (coverage retrieval, pose-guided fusion).

### Theory-Practice Gap Assessment
There are no major theoretical proofs that could conflict with practice. The paper is primarily an empirical systems paper. The assumption that local 3D point clouds are "cleaner" is practically true in terms of fusion noise, but they still contain single-view depth estimation errors. The paper correctly acknowledges this and designs the multi-anchor controller specifically to mitigate these residual inconsistencies.

### Overall Technical Soundness Verdict
Sound with minor issues

### Score
7.0
