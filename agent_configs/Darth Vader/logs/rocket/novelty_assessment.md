### Claimed Contributions
1. **ROCKET Framework**: A multi-layer representation alignment method to inject 3D spatial reasoning into 2D-pretrained Vision-Language-Action (VLA) models using a single layer-invariant shared projector.
2. **Gradient Interference Mitigation**: Theoretical and empirical analysis demonstrating that using multiple independent projectors for multi-layer alignment causes severe gradient conflicts, and that a shared projector mitigates this by aligning one residual stream to another constructively.
3. **Matryoshka-style Sparse Activation**: A nested sparse-activation mechanism to balance alignment losses across depths, preventing shallow layers (which converge easier) from dominating the shared projector.
4. **Computational Efficiency**: Reaching state-of-the-art performance on LIBERO benchmarks with only ~4% of the compute required by prior alignment methods.

### Prior Work Assessment
- **Spatial Grounding in VLAs**: Prior works (e.g., Spatial Forcing) align VLA representations with 3D foundation models at a *single* layer. This requires extensive post-hoc search to identify the optimal layer. ROCKET's use of multi-layer alignment avoids this search and captures hierarchical features. The delta is substantial: moving from a fragile single-layer search to a robust multi-layer formulation.
- **Multi-Layer Distillation**: Distilling from multiple layers is common in vision and language models (e.g., FitNets). However, ROCKET's observation that independent projectors fail in VLA models due to gradient orthogonalization is insightful. Adapting a *shared* projector to enforce constructive interference under Pre-LN transport is a non-trivial adaptation to the VLA setting.
- **Matryoshka Representation Learning**: Matryoshka learning typically enforces nested representations within a single embedding. ROCKET creatively re-purposes this concept to dynamically modulate the capacity of a shared projector depending on the network depth, preventing early convergence of shallow layers.

### Novelty Verdict
Substantial

### Justification
The paper combines several existing concepts—multi-layer distillation, Matryoshka representations, and spatial alignment—in a novel and highly effective way. The theoretical framing of how independent projectors lead to gradient interference in residual networks (and how shared projectors alleviate it) provides a strong scientific foundation. While the individual components are not entirely unprecedented, their creative combination addresses a critical bottleneck in VLA training (inefficient layer search and representation collapse), making the contribution clearly distinct and non-obvious.

### Missing References
None critical. The paper adequately cites prior works in VLA representation alignment, 3D foundation models, and general distillation.

Score: 5.5 / 10
