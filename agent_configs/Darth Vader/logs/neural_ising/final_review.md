## Review: Neural Ising Machines via Unrolling and Zeroth-Order Training

This paper proposes a highly scalable, data-driven optimization method for solving NP-hard Ising and Max-Cut problems. The core contribution is the Neural Parameterized Ising Machine (NPIM), which unrolls the iterative dynamical updates of classical Ising machines and parameterizes the node-wise update rules using a compact multilayer perceptron (MLP). To avoid the instabilities of backpropagation through time (BPTT) over long recurrent optimization trajectories, the authors creatively employ a zeroth-order evolutionary optimizer to learn time-varying network parameters via a Fourier basis. 

### Novelty
The paper introduces a substantial contribution by moving away from heavily parameterized neural combinatorial optimization models (e.g., GNNs, Diffusion models) towards learning highly localized update heuristics. While algorithm unrolling (L2O) is well-known for convex problems (e.g., LISTA), adapting it to non-convex combinatorial optimization by parameterizing an Ising machine's spin update dynamics with a tiny MLP is a highly creative and effective synthesis. The explicit avoidance of BPTT in favor of a zeroth-order optimizer from recent literature elegantly solves the chaotic gradient problem in unrolled Ising systems. The novelty is strong because the methodology directly challenges the current trend of massive models for CO, replacing them with a ~50 parameter model that learns time-varying schedules and momentum.

### Technical Soundness
The technical foundation is sound and well-reasoned. The formulation of the NPIM restricts the MLP to process only a finite history of local coupling fields, maintaining permutation equivariance across nodes. The paper correctly implements the $Z_2$ symmetry of the Ising model by omitting bias parameters and utilizing odd activation functions ($\tanh$). Using zeroth-order optimization perfectly circumvents the well-documented gradient issues associated with long recurrences. The empirical claims that the network learns momentum-like behavior to escape local minima are backed by an analysis of the evolving weights during training. 

### Experimental Rigor
The experiments are mostly rigorous, mapping well to the paper's claims. The authors perform comprehensive evaluations on both neural CO benchmarks (MIS, Max-Clique, Max-Cut graphs) and standard Ising machine benchmarks (G-set). The baselines are strong and highly relevant, contrasting NPIM with both state-of-the-art diffusion samplers (SDDS, DiffUCO) and classical dynamical solvers (dSBM, CAC). 

There is, however, a slight gap in statistical rigor. In Table 1, while baselines are reported with standard deviations, the dNPIM results are presented as point estimates without variance metrics. Furthermore, the reliance on a "top 30" parallel run budget makes direct wall-clock timing comparisons tricky. The authors acknowledge that dNPIM runs significantly slower on large graphs (1:20 vs 0:02 for SDDS), attributing this to dense PyTorch matrices vs sparse implementations, which leaves some ambiguity regarding the intrinsic computational complexity of the learned heuristic.

### Impact
This work possesses substantial technical and scientific significance. By proving that a minimal, ~50-parameter neural network can act as a highly effective update rule for complex combinatorial problems, the authors provide a highly scalable, easily adoptable drop-in solver. The scientific insight that unrolled Ising dynamics can be effectively tuned via evolutionary algorithms is an important lesson that extends beyond this specific application. As researchers look for more computationally efficient alternatives to diffusion models for CO, this lightweight approach is well-positioned to serve as an important baseline and a foundation for future iterative solvers. 

### Scoring Breakdown
- **Novelty:** 7.0
- **Technical Soundness:** 8.0
- **Experimental Rigor:** 6.0
- **Impact:** 7.0

**Formula:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Calculation:** (28.0 + 16.0 + 12.0 + 14.0) / 10 = 7.0
**Final Review Score:** 7.0
