This paper introduces a novel perspective on autoregressive self-attention, reframing it as a dynamic, two-layer Multi-Layer Perceptron (MLP) where the context history length acts as an ever-growing hidden dimension. From this theoretical foundation, the authors propose HyperMLP and HyperGLU, new attention variants that explicitly learn input-conditioned sequence-dimension mixing alongside standard feature-dimension mixing, and provide theoretical insights into established Transformer design principles. 

### Novelty

The paper's contributions to novelty can be separated into its theoretical reframing and its architectural innovations. 

**Conceptual Reframing of Attention:** The idea of viewing attention as generating data-dependent fast weights or utilizing ReLU to treat attention scores as unbounded gating activations rather than a probability simplex has been previously explored by works like Schlag et al. (2021) and Wortsman et al. (2023). The novelty here lies not in these individual components, but in their synthesis into a cohesive "3-stage memory view" (Global Space $\to$ Pool $\to$ Activated Memory). This taxonomy provides a refreshing theoretical lens to unify various attention mechanisms, representing a moderate delta over prior work.

**HyperMLP / HyperGLU Architecture:** The paper extends recent trends in sequence mixing (like the diagonal temporal gating seen in GLA) by introducing a dense, low-rank input-conditioned mixing matrix applied to a lag-ordered history. While this cross-positional mixing creates a "warped routing geometry", the approach relies on fixed maximum-length tensors and essentially inserts a data-dependent linear layer across the sequence dimension within the standard quadratic computation. This represents a sensible but moderate architectural evolution. It should be noted that Synthesizer (Tay et al., 2020) explicitly explored learning dense sequence mixing matrices, a highly relevant prior work missing from the paper's references.

**Theoretical Insights into Design Principles:** The most substantial novelty lies in the paper's theoretical insights. The authors leverage their dynamic-MLP framing to formally prove (Theorem 2.5) why shrinking the readout core (VO) constrains the update subspace dimension, while shrinking the routing core (QK) only restricts conditioning geometry. This rigorous mathematical foundation for previously empirical heuristics regarding LoRA adapter placement and QK vs. VO projections is highly valuable to the community.

### Technical Soundness

The paper is exceptionally rigorous and technically sound, with a remarkably small theory-practice gap. The theoretical derivations are algebraically exact, and the empirical ablations are meticulously designed to test specific mathematical claims.

**Theoretical Claims and Verifications:** The algebraic refactoring of autoregressive attention into a dynamic two-layer MLP is exact. The paper mathematically confirms that input-dependent sequence mixing warps gating hyperplanes, expanding the function class. Furthermore, Theorem F.1 rigorously proves that canonical sequence mixing extensions only match autoregressive generation when using the proposed newest-to-oldest lag layout. The rank allocation asymmetry theorem correctly applies linear algebra properties to validate shrinking QK over VO. The GLU-style modulation is also correctly shown to decouple gating from magnitude without flipping the gate's binary state.

**Computational and Empirical Soundness:** The computational complexity analysis correctly verifies that the Diagonal-Plus-Low-Rank (DPLR) mixing evaluates efficiently without materializing full $t \times t$ matrices. Empirically, the ablation study systematically isolates the effects of sequence mixing and the lag layout, employing matched-parameter budgets that enforce the zero-sum trade-offs predicted by the theory. 

A minor concern is the reliance on a depthwise convolution in the default HyperMLP implementation, which slightly convolutes the pure "dense sequence mixing" narrative. However, the authors transparently disclose this and show that convolution-free variants still significantly outperform baselines.

### Experimental Rigor

The experimental design is mostly rigorous, featuring outstanding baseline construction and a masterclass ablation study, though it suffers from a lack of statistical variance reporting and qualitative error analysis.

**Baselines and Ablations:** The baselines are exceptionally strong and fair, trained from scratch under identical conditions and strictly matched parameter budgets to enforce zero-sum tradeoffs. The Controlled Design Study on MAD and NanoGPT systematically isolates every architectural component, proving claims that Softmax is not essential, sequence mixing provides dominant expressive gains, and the lag layout is strictly necessary for autoregressive consistency. 

**Datasets and Metrics:** The chosen datasets are appropriate, using MAD for mechanistic probing and NanoGPT/FineWeb-Edu for language modeling up to 1.3B parameters, evaluated on the Open LLM Leaderboard. The metrics perfectly align with the empirical claims.

**Missing Rigor:** The most significant flaw is the absence of standard deviations or confidence intervals. While multiple seeds at 1.3B parameters are expensive, they are expected for the smaller-scale NanoGPT ablations to prove statistical significance. Additionally, the paper lacks a qualitative error analysis to characterize failure modes or demonstrate where HyperMLP specifically improves upon baselines in downstream tasks. A scaling law plot (FLOPs vs. Loss) would also help characterize performance trajectories.

### Impact

**Scientific Significance:** The conceptual reframing of autoregressive attention as an ever-growing dynamic MLP is scientifically valuable. By providing a principled explanation for empirical folklore (like QK vs. VO compression and LoRA placement), this theoretical framework may influence how researchers mathematically analyze and design future sequence routing mechanisms.

**Technical Significance and Adoption:** Despite the impressive matched-parameter performance gains, the practical real-world impact of HyperMLP is currently limited. The method introduces $O(T^2 r_s)$ overhead per head and modifies the attention operator such that it is incompatible with highly optimized hardware kernels like FlashAttention. In an era dominated by memory bandwidth bottlenecks and a trend toward sub-quadratic sequence models, a heavier quadratic alternative without a fused kernel is unlikely to see immediate adoption by practitioners for foundation model training. The method will remain of academic interest until these critical systems-level deployment barriers are addressed.

### Scoring Breakdown
- **Novelty:** 6.5 / 10
- **Technical Soundness:** 9.5 / 10
- **Experimental Rigor:** 7.5 / 10
- **Impact:** 4.0 / 10

**First Review Score Formula:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 6.3 / 10