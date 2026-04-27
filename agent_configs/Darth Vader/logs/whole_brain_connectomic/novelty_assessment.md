### Claimed Contributions
1. **Connectome-Structured Architecture**: The development of FlyGM, a dynamic neural controller that uses the exact topology of the adult Drosophila whole-brain connectome as a message-passing graph for reinforcement learning.
2. **Diverse Embodied Locomotion**: The successful application of FlyGM to control a high-fidelity biomechanical fruit fly model (flybody) across multiple locomotion tasks, including walking, turning, and flight.
3. **Evidence of Structural Inductive Bias**: Empirical demonstration that the biological connectome provides a superior structural inductive bias for embodied control compared to random graphs, degree-preserving rewired graphs, and standard MLPs, yielding higher sample efficiency and performance.

### Prior Work Assessment
- **Connectome-constrained RL for embodied control**: Prior work has explored connectome-constrained networks, but largely for smaller organisms (e.g., C. elegans connectome in Zhao et al., 2024; Lechner et al., 2020) or specific subsystems of the fly (e.g., visual system in Lappalainen et al., 2024; motor circuits in Shiu et al., 2024; Lesser et al., 2024). The integration of the entire adult Drosophila connectome (~140k neurons) to control a full biomechanical body across diverse locomotor tasks is a massive leap in scale and complexity.
- **Biomechanical Fruit Fly Models**: The 'flybody' environment (Vaxenburg et al., 2025) recently introduced the MuJoCo simulation of the fly, but it relies on hand-crafted MLP policies. Replacing the MLP with the biological connectome topology represents a substantial conceptual and methodological step towards biologically realistic artificial agents.
- **Graph Neural Networks for Control**: While GNNs are common in RL, instantiating the specific wiring of a biological brain—and explicitly demonstrating that the evolved topology outperforms degree-preserving rewired graphs—is a profound and highly novel scientific insight.

### Novelty Verdict
Substantial

### Justification
The paper represents a major milestone in the intersection of connectomics and embodied AI. While the physics simulator (flybody) and the connectome (FlyWire) were recently published independently, bringing them together to close the sensorimotor loop using the whole-brain wiring diagram is highly original. The methodology of using the connectome as a GNN isn't entirely new conceptually (it has been done for visual processing and C. elegans), but the scale and application to whole-body 3D locomotion of an insect are unprecedented. Furthermore, the ablation against a degree-preserving rewired graph offers a rigorous and novel piece of scientific evidence that the specific biological wiring matters.

### Missing References
None critical. The paper appropriately cites the recent foundational works (FlyWire Dorkenwald et al., 2024; flybody Vaxenburg et al., 2025).

### Score
7.5
