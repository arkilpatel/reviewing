# Review: Sparse Training of Neural Networks based on Multilevel Mirror Descent

## Novelty & Originality
### Claimed Contributions
1. A dynamic sparse training algorithm based on linearized Bregman iterations (mirror descent) that alternates between static sparsity pattern updates (coarse steps) and dynamic sparsity pattern updates (fine steps).
2. The embedding of this algorithm into a multilevel optimization framework, utilizing restriction and prolongation operators to map between the fine (dense) and coarse (sparse) levels.
3. Convergence guarantees for the algorithm, proving sublinear convergence under the assumption of a Polyak-Lojasiewicz (PL)-type inequality.
4. Empirical results demonstrating that the method achieves high sparsity and accuracy on CIFAR-10 and TinyImageNet, along with theoretical FLOP reductions compared to standard linearized Bregman iterations.

### Prior Work Assessment
- **Dynamic Sparse Training via Alternating Dense/Sparse Phases:** The core idea of alternating between a fully dense optimization step (to explore new parameters) and sparse optimization steps (to train the active subnetwork) is well established. Methods like AC/DC (Peste et al., 2021) utilize alternating phases of full-support and sparse-support optimization. Similarly, RigL (Evci et al., 2020) and Top-KAST (Jayakumar et al., 2020) rely on periodic dense gradient computations to update the sparsity mask while mostly training a sparse subnetwork. The delta here is primarily the specific use of mirror descent as the base optimizer rather than SGD/Adam.
- **Bregman Iterations for Sparse Training:** The method is a direct extension of LinBreg (Bungert et al., 2022). LinBreg already applies stochastic linearized Bregman iterations with a non-smooth mirror map to induce unstructured sparsity during neural network training. The delta from LinBreg is merely the algorithmic decision to freeze the non-zero parameters for $m$ iterations (the "coarse" phase) before computing another full dense gradient. 
- **Multilevel Optimization Formulation:** Framing the freezing of inactive weights as a "coarse" level in a multilevel optimization hierarchy (building on ML BPGD by Elshiaty & Petra, 2025) provides a nice theoretical abstraction. However, practically, it just formalizes a masking operation. 

### Novelty Verdict
Incremental

### Justification
The paper introduces a mathematically elegant formulation (multilevel mirror descent) for a practice that is already standard in dynamic sparse training: freezing the sparsity mask for several steps to save compute, and periodically computing dense gradients to allow the sparsity pattern to evolve. The foundation of using Bregman iterations for sparsity is already established by LinBreg (Bungert et al., 2022). The proposed "ML LinBreg" is essentially LinBreg applied with an alternating mask-update schedule. While the multilevel optimization framing is conceptually interesting, it does not yield a fundamentally new capability or paradigm shift. The resulting algorithm behaves very similarly to existing dynamic sparse training algorithms.

### Missing References
The related work is generally adequate, but it should draw stronger explicit connections to AC/DC (Peste et al., 2021) in the methodological design, as AC/DC's alternating dense/sparse phases are highly analogous to the proposed fine/coarse levels.

4.0


## Technical Soundness
### Claims Inventory
1. **Theoretical:** The coarse objective $\hat{L}^{(k)}$ is $L$-smooth relative to the coarse regularizer $\hat{J}_{\delta}^{(k)}$.
2. **Theoretical:** Restricting fine-level subgradients yields valid coarse-level subgradients, and prolongating coarse-level subgradients yields valid fine-level subgradients (Propositions 3.1 and 3.2).
3. **Theoretical:** The proposed multilevel LinBreg algorithm achieves sublinear convergence in expectation assuming exact gradients on the fine level, stochastic unbiased gradients on the coarse level, and a Polyak-Łojasiewicz (PL)-type inequality (Theorem 4.1).
4. **Empirical:** The algorithm successfully reduces theoretical FLOPs while matching the accuracy and sparsity of baseline methods like LinBreg and RigL.

### Verification Results
1. **Coarse Objective Smoothness:** Verified. The proof in Lemma A.1 correctly leverages the linearity of the restriction/prolongation operators.
2. **Subgradient Transfer:** Verified. Propositions 3.1 and 3.2 are technically correct due to the separable block structure of the regularizer.
3. **Convergence Rate:** Error Found / Significant Concern (Theory-Practice Gap). The theorem statement strictly assumes access to exact, full-batch gradients on the fine level ($\nabla L(\theta)$). 
4. **Empirical FLOP Reduction:** Verified theoretically, but computationally misleading as unstructured sparsity does not easily translate to FLOP reductions on modern hardware without specialized libraries.

### Errors and Concerns
1. **Severe Theory-Practice Gap in Convergence Guarantee (Significant Concern):** Theorem 4.1 requires exact, full-batch gradients computed over the entire training dataset for every "fine" level update. In modern deep learning, computing the exact full gradient over the dataset is computationally intractable. The authors explicitly acknowledge this limitation in Section 4: "we assume that these gradient estimators are unbiased... we use the exact gradients on the fine level... ultimately, we would like to prove the same results when also using stochastic gradients on the fine level. However, this appears to be out of reach". Yet, in the experiments (Section 5), they explicitly use mini-batch stochastic gradients on the fine level. Therefore, the central theoretical result of the paper does not apply to the algorithm actually implemented and evaluated. 
2. **Strong PL-Inequality Assumption (Concern):** Assumption 2 requires a variant of the Polyak-Łojasiewicz inequality to hold globally for the deep neural network loss function relative to the Bregman divergence. This is an exceptionally strong assumption that is widely known to be violated in non-convex deep neural network training. While standard in some optimization literature, claiming convergence for neural networks based on this assumption is somewhat vacuous in practice.

### Internal Consistency Check
The paper is mostly internally consistent in its notation and mathematical derivations. The proofs in the appendix logically follow from the stated assumptions.

### Theory-Practice Gap Assessment
The theory-practice gap is the most significant flaw in the paper's technical soundness. The entire multilevel convergence proof hinges on the fine-level problem acting as a deterministic anchor (exact gradients) to correct the stochastic coarse-level steps. By substituting stochastic mini-batch gradients at the fine level in the experiments, the theoretical guarantees are entirely voided. 

### Overall Technical Soundness Verdict
Significant concerns

4.0


## Experimental Rigor
### Claims-to-Experiments Mapping
1. **Claim:** The method produces highly sparse and accurate models. **Experiment:** ResNet18, VGG16, and WideResNet28-10 on CIFAR-10 and TinyImageNet compared against LinBreg, RigL, and Pruning. (Supported)
2. **Claim:** The method reduces the theoretical number of FLOPs required for training. **Experiment:** Theoretical FLOP calculations provided in Appendix C, and a CPU-based wall-clock time comparison using SparseProp. (Partially supported; CPU only).

### Baseline Assessment
The baselines include standard SGD, LinBreg, RigL, and Prune+Fine-Tuning. 
- **Tuning & Fairness:** The pruning baseline is given 180 epochs of dense training followed by 20 epochs of fine-tuning, matching the 200-epoch budget of the proposed method. However, RigL heavily relies on the ERK mask initialization to perform well, whereas the proposed method uses a variance-preserving uniform initialization. 
- **Missing Baselines:** The paper misses comparisons with state-of-the-art alternating or dynamic sparse training algorithms that do exactly what this paper proposes (alternating dense/sparse phases), most notably AC/DC (Peste et al., 2021). 

### Dataset Assessment
The paper evaluates exclusively on CIFAR-10 and TinyImageNet. In the current landscape of sparse training research, these datasets are considered toy benchmarks. TinyImageNet is a scaled-down dataset that does not exhibit the same optimization dynamics as full-scale datasets. Standard evaluation for sparse neural network training mandates ImageNet-1K. The lack of ImageNet-1K evaluation is a significant gap in experimental rigor.

### Metric Assessment
The metrics are Test Accuracy and Sparsity. These are standard and appropriate. Theoretical FLOPs are also reported. However, theoretical FLOPs for *unstructured* sparsity are well-known to be highly misleading because standard GPUs cannot accelerate unstructured sparse matrix multiplications efficiently. The authors attempt to address this by showing wall-clock speedups on a CPU using `SparseProp`, but deploying deep neural networks on CPUs for training is practically irrelevant in modern ML.

### Statistical Rigor
The authors report mean values over multiple random seeds, and plots (e.g., Figure 5) show shaded variance regions. This indicates good statistical hygiene. However, the comparisons in Figure 1 and Table 1 often show overlapping error margins, making it difficult to confidently assert that ML LinBreg is statistically superior to RigL or LinBreg, but rather that it is roughly equivalent.

### Ablation Assessment
The paper provides ablations over the regularization strength $\lambda$ and the coarse-period duration $m$. These ablations adequately isolate the effect of the multilevel scheduling. However, the choice of $m=99$ (1 dense step per 100 sparse steps) is quite extreme and seems to be selected primarily to minimize theoretical FLOPs.

### Missing Experiments
1. **ImageNet-1K Evaluation:** Mandatory for any modern sparse training algorithm to prove scalability and practical utility.
2. **State-of-the-Art Baselines:** Comparison with AC/DC, Top-KAST, or more recent dynamic sparse training methods.
3. **Hardware Acceleration:** Real-world GPU throughput measurements (even if just memory savings) rather than just theoretical FLOPs or CPU timings.

### Error Analysis Assessment
The paper lacks an error analysis. There is no investigation into *what* is being pruned or how the sparsity pattern evolves over the course of the fine/coarse alternation. 

### Overall Experimental Rigor Verdict
Significant gaps

4.0


## Significance & Impact
### Impact Assessment

**1. Technical Significance (70%):**
The practical utility of this method is severely limited by its focus on unstructured sparsity. The authors demonstrate that "ML LinBreg" can match the accuracy of RigL and LinBreg while utilizing fewer "theoretical FLOPs." However, unstructured sparsity does not translate to wall-clock acceleration on modern hardware accelerators (GPUs/TPUs) without specialized, often non-standard libraries (like the CPU-only `SparseProp` used in the paper). Consequently, practitioners are highly unlikely to adopt this method to speed up training, as the overhead of managing dynamic unstructured masks on a GPU typically outweighs the compute savings. Furthermore, the empirical performance on CIFAR-10 and TinyImageNet only shows marginal, if any, improvements over existing methods like RigL. Without demonstrating utility on large-scale datasets (ImageNet-1K) or large language models, the adoption potential is exceedingly low.

**2. Scientific Significance (30%):**
The scientific contribution lies in framing the well-known heuristic of alternating between dense gradient updates and sparse mask freezing as a "multilevel mirror descent" optimization problem. This provides a clean theoretical abstraction for why freezing the network structure during sparse training is mathematically justified. However, this theoretical contribution is heavily undermined by the necessity of assuming exact, full-batch gradients on the fine level to prove convergence. Since deep learning relies entirely on stochastic gradients, the theoretical framework does not accurately describe the empirical practice. Therefore, it is unlikely to fundamentally shift how researchers analyze non-convex sparse optimization.

**3. The 3-Year Citation Projection:**
This paper will likely receive very few citations (e.g., < 10 in the next 3 years). The core idea of alternating sparse and dense phases is already heavily explored by heavily cited papers like AC/DC and RigL. The theoretical angle is compromised by the exact-gradient assumption, and the empirical results do not push the state-of-the-art forward on standard large-scale benchmarks. It may be cited briefly in reviews of mirror descent applications to deep learning, but it will not become a foundational or highly influential work.

**Impact Score: 3.5 / 10**


## Scoring Breakdown
- **Novelty:** 4.0
- **Technical Soundness:** 4.0
- **Experimental Rigor:** 4.0
- **Impact:** 3.5

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 3.8
