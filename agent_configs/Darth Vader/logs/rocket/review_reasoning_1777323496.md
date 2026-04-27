# Final Review: ROCKET

This paper introduces ROCKET, a residual-oriented multi-layer alignment framework designed to inject 3D spatial reasoning into 2D-pretrained Vision-Language-Action (VLA) models. The core idea is to move away from computationally expensive single-layer alignment searches by utilizing a multi-layer distillation approach. To circumvent the severe gradient interference caused by independent layer-wise projectors, the authors propose a single, shared projector combined with a Matryoshka-style sparse activation scheme. 

### Novelty
The paper combines several existing concepts—multi-layer distillation, Matryoshka representations, and spatial alignment—in a highly effective and clever way. While distilling representations from multiple layers is a common technique in computer vision (e.g., FitNets), ROCKET's observation that independent projectors fail in VLA models due to gradient orthogonalization is an insightful contribution. Adapting a shared projector to enforce constructive interference under Pre-LN transport is a non-trivial and mathematically well-grounded adaptation to the VLA setting. Furthermore, creatively re-purposing Matryoshka learning to dynamically modulate the capacity of the shared projector based on network depth is a clever structural solution to prevent shallow layers from dominating the alignment. The novelty delta here is substantial, effectively shifting the paradigm from fragile single-layer searches to robust multi-layer alignment.

### Technical Soundness
The paper's technical foundation is sound, supported by both theoretical proofs and empirical verification. The authors' claim that naive multi-layer alignment causes gradient interference is convincingly verified through empirical visualizations (e.g., gradient cosine similarity dropping to near zero). The proposed solution of a shared projector is theoretically justified in Appendix H, where the authors derive the gradient flow through Pre-LN residual blocks to demonstrate constructive cross-layer interference. While the proof relies on strong assumptions—such as perfectly bounded residual increments and "near-isometry on the error-signal subspace," which are difficult to guarantee during the non-convex optimization of 7B-parameter models—the empirical CKA similarity adequately bridges this theory-practice gap. The design aligns cleanly with the observed behavior of the gradients, making the claims logically sound despite minor concerns regarding the rigidity of the theoretical bounds.

### Experimental Rigor
The experimental design is mostly rigorous, leveraging strong and highly relevant simulation benchmarks (LIBERO, LIBERO-Plus, and RoboTwin 2.0). The baselines are competitive, actively utilizing the best reported configurations for prior state-of-the-art single-layer methods (like Spatial Forcing). The ablation studies are well-constructed, cleanly isolating the multi-layer independent projector approach to confirm its detrimental impact (dropping performance to 80.0%) and demonstrating how the shared projector successfully rescues and improves it (98.5%). 

However, there are notable gaps in the empirical rigor. Chief among these is the complete absence of real-world robotic experiments. For a paper focused explicitly on improving 3D spatial alignment in physical manipulation, simulation results—even those targeting spatial shifts like LIBERO-Plus—cannot fully replicate the noisy, uncalibrated dynamics of the real world. Additionally, while the evaluation correctly aggregates variance across 100 evaluation rollouts, the paper fails to report standard deviations or variance across multiple *training seeds*. Given the competitive 2% margin over the baselines, establishing the statistical significance of the training runs is a missing piece.

### Impact
ROCKET presents high technical utility for the robotics and vision-language communities. Fine-tuning massive VLA models is notoriously bottlenecked by immense computational requirements. By eliminating the need for hyperparameter sweeping to find the optimal distillation layer, ROCKET achieves state-of-the-art spatial alignment using only ~4% of the compute budget required by previous methods. This makes 3D spatial alignment highly accessible. The framework is elegant and acts as a generic drop-in replacement that has proven to generalize across disparate VLA architectures (OpenVLA, PI0). Scientifically, the insight into cross-layer gradient coherence under Pre-LN transport provides a useful framework that can be adopted by the broader representation learning community. It is highly likely that ROCKET will see strong adoption and citations as the field continues to scale multimodal embodied models.

### Scoring Breakdown
- **Novelty:** 5.5 / 10
- **Technical Soundness:** 6.0 / 10
- **Experimental Rigor:** 5.0 / 10
- **Impact:** 5.5 / 10

**Score Formula:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Review Score:** 5.5
