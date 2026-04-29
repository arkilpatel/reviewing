### Claimed Contributions
1. A new data-driven heuristic for NP-hard Ising and Max-Cut problems called Neural Parameterized Ising Machine (NPIM).
2. Parameterizing the node-wise update rule of an iterative dynamical system using a compact multilayer perceptron (MLP) with time-varying weights defined via a Fourier basis.
3. Training the recurrent dynamics using a zeroth-order evolutionary optimizer to avoid the instability of backpropagation through time.
4. Empirical demonstration that the learned dynamics recover momentum-like behavior and time-varying schedules, achieving competitive or state-of-the-art results on several benchmarks.

### Prior Work Assessment
- **Algorithm Unrolling (L2O)**: Unrolling iterative algorithms and parameterizing them as recurrent networks is well-established for convex problems (e.g., LISTA). The authors extend this to the non-convex Ising problem domain. This represents a solid, though somewhat predictable, extension.
- **Zeroth-Order Training**: The authors explicitly state they rely on the zeroth-order optimization method from Reifenstein et al., 2024. The training algorithm itself is not their core contribution, but applying it to train a learned Ising machine update rule effectively circumvents the well-known issues of BPTT in chaotic/recurrent systems.
- **Deep Learning for CO**: Prior approaches (GNNs, Transformers, Diffusion models like Sanokowski et al., 2025) typically operate on the whole graph and require large parameters. By contrasting this with a node-wise, shared-weight MLP, the authors introduce a highly scalable, minimalist approach.

### Novelty Verdict
Substantial

### Justification
The paper combines several existing concepts—algorithm unrolling, dynamical Ising machines, and zeroth-order optimization—in a non-obvious and highly effective way. Parameterizing the update rule with a tiny MLP that learns time-varying parameters via a Fourier basis, and specifically dodging the backpropagation issues by employing a zeroth-order optimizer, yields a fundamentally different approach compared to the heavily parameterized GNN/Diffusion models popular in current literature. While the individual components (MLP, Fourier basis, zeroth-order optimizer) are known, their synthesis to create a scalable, learned Ising machine is a substantial conceptual and methodological contribution.

### Missing References
The related works section appears quite comprehensive, covering both neural combinatorial optimization and classical/dynamical Ising machines.

### Score
7
