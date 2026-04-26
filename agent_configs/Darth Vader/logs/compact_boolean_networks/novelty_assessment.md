### Claimed Contributions
1. An efficient connection learning strategy for Boolean networks that introduces no additional parameter matrices, relying instead on weight entropy tracking and adaptive resampling.
2. A compact convolutional Boolean architecture that removes the need for hardcoded Boolean trees by leveraging the learned connections to aggregate information.
3. An adaptive discretization strategy that progressively freezes and discretizes layers (specifically convolutional ones) during training to close the relaxation-discretization gap.

### Prior Work Assessment
- Differentiable learning of Boolean networks is an established but challenging subfield (e.g., DiffLogicNet by Petersen et al., 2022).
- Previous methods either used random fixed connections (inefficient due to extreme sparsity) or parameterized full routing matrices (incurring quadratic memory/compute costs). The adaptive resampling approach is a highly practical middle ground.
- Adaptive or progressive quantization/discretization is a widely known technique in the neural network quantization literature, but its specific application here guided by layer-wise entropy convergence is a neat adaptation for logic networks.

### Novelty Verdict
Moderate

### Justification
The paper does not introduce a fundamentally new paradigm for learning Boolean networks, as it builds heavily on the continuous relaxation framework of DiffLogicNet. However, the three proposed algorithmic improvements are clever, synergistic, and specifically tailored to address the known bottlenecks of logic networks. The combination of entropy-guided resampling to implicitly learn routing without parameter bloat is the most novel and elegant contribution of the three.

Score: 6.0