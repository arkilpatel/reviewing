# Review: Enabling Progressive Whole-slide Image Analysis with Multi-scale Pyramidal Network

## Novelty & Originality
### Claimed Contributions
1. **Grid-based Remapping**: A method that uses high-magnification (e.g., 20x) patch-level features from foundation models to derive coarse, lower-magnification feature maps. This is claimed to bypass the need for explicitly extracting features at multiple predetermined magnifications (e.g., 5x, 10x).
2. **Coarse Guidance Network (CGN)**: A lightweight convolutional network that processes the generated coarse feature maps to learn contextual guidance, using a grid-wise sigmoid attention mechanism.
3. **Multi-scale Pyramidal Network (MSPN)**: A plug-and-play module connecting multiple CGNs residually across different fields-of-view (FOVs) to enable progressive, multi-scale contextual learning for existing attention-based Multiple Instance Learning (MIL) frameworks.

### Prior Work Assessment
- **Multi-scale MIL in CPath**: Prior works like HAG-MIL, DSMIL, and cross-scale attention networks typically require extracting patches at multiple physical magnifications (e.g., 5x, 10x, 20x). The paper rightly points out that this is computationally expensive and rigid. The delta here is utilizing only 20x features to synthesize the lower scales. 
- **Spatial Pooling & Pyramids**: The core of "grid-based remapping" is essentially spatial average pooling of patch tokens based on their 2D coordinates. Creating feature pyramids via spatial pooling is a foundational concept in computer vision (e.g., Spatial Pyramid Pooling (SPP), Feature Pyramid Networks (FPN)). Applying this to unordered MIL patch bags by projecting them back to a 2D grid is a logical, albeit highly predictable, extension.
- **Delta**: The conceptual gap between standard spatial average pooling and this paper's "Grid-based Remapping" is minimal. The main novelty lies in the *creative combination* of this pooling with a lightweight residual CNN (the CGN) to inject coarse spatial priors back into the patch-level attention weights of an standard MIL framework (like ABMIL or CLAM). 

### Novelty Verdict
Incremental

### Justification
While the engineering execution is neat and highly practical, the underlying methodological novelty is incremental. Deriving "coarse" features by average-pooling high-resolution features within a spatial grid is a standard technique. The paper rebrands this spatial downsampling as "grid-based remapping". The CGN itself is a standard 3-layer CNN (Conv3x3 -> Conv3x3 -> Conv1x1) applied to the pooled grid. The combination provides a useful architectural add-on, but it does not represent a fundamentally new paradigm or mathematical framework. The primary contribution is an empirical demonstration that spatial pooling + local convolutions can effectively substitute for explicit multi-scale feature extraction in the era of CPath foundation models.

### Missing References
The paper lacks references to fundamental spatial pyramid pooling (SPP) and feature pyramid literature in general computer vision, which forms the core basis of their grid-remapping strategy.

4.0


## Technical Soundness
### Claims Inventory
1. **Theoretical/Methodological**: Grid-based remapping mathematically maintains the MIL formulation while downsampling bag-level features into a coarser scale.
2. **Theoretical/Complexity**: MSPN's computational complexity is linear with respect to the patch number $N$ and the number of FOVs $k$, avoiding the quadratic complexity of self-attention.
3. **Empirical**: MSPN consistently improves attention-based MIL frameworks across multiple tasks, foundation models, and datasets.
4. **Conceptual**: MSPN's coarse guidances focus progressively from global to local tumor structures.

### Verification Results
1. **Grid-based remapping formulation**: Verified. The derivation (Eq 1 to Section 3.2) correctly shows that average pooling subsets of a bag corresponds to a valid MIL aggregation step. 
2. **Complexity claim**: Verified. The convolution operations over the downsampled grids $H' \times W'$ and the element-wise multiplications indeed scale linearly with $N$, making it significantly faster than transformer-based multi-scale methods like HAG-MIL or TransMIL.
3. **Empirical improvements**: Verified (with minor concerns). The tabular results support the claim that MSPN outperforms single-scale and simple concatenation baselines.
4. **Conceptual/Interpretability**: Unverifiable/Concern. The heatmap visualizations (Figure 4) show alignment, but this is a qualitative evaluation on cherry-picked examples.

### Errors and Concerns
- **Minor Error / Concern (Feature Representation Gap)**: The paper operates under the unverified assumption that average-pooling 20x patch embeddings perfectly mimics the representation of a native 5x or 10x patch embedding. Foundation model representations (like UNI2 or CONCH) are highly non-linear. The average of four 20x patch embeddings is mathematically distinct from the embedding of one 10x patch passed through the same ViT. While the empirical results show this pseudo-coarse feature is useful, the paper glosses over this representational gap.
- **Concern (SHAP Analysis Applicability)**: In Appendix G, SHAP values are used to compare feature importance between concatenation and MSPN. However, MSPN is a residual network that intrinsically mixes scales through addition ($H = H + H_k$). Comparing SHAP values of mixed residual features against cleanly separated concatenated features can be mathematically misleading due to the overlapping feature spaces.

### Internal Consistency Check
The mathematical formulation in the text aligns with the pseudocode provided in the appendices. The reported parameter counts and FLOPs in Table 1 correctly reflect the lightweight nature of the proposed CGN blocks. There are no glaring contradictions in the text.

### Theory-Practice Gap Assessment
The primary theory-practice gap lies in the aforementioned assumption that spatially averaged high-res features are a 1-to-1 substitute for actual low-res visual context. The experiments prove they are a *useful* substitute, but the theoretical equivalence is neither claimed nor proven, which slightly weakens the foundation of the grid-remapping motivation.

### Overall Technical Soundness Verdict
Sound with minor issues

6.5


## Experimental Rigor
### Claims-to-Experiments Mapping
1. **MSPN improves general MIL performance**: Supported by Table 1 (comparison across 4 frameworks, 3 FMs, 4 tasks).
2. **MSPN is computationally efficient**: Supported by Table 1 (Params/FLOPs), Figure 3, and Appendix F (Runtime scaling).
3. **MSPN is effective with pre-trained MIL models**: Supported by Table 2.
4. **Multiple scales progressively help**: Supported by Table 3 (Ablation on number of FOVs).

### Baseline Assessment
The baselines are strong and appropriate. The authors test across multiple widely adopted MIL frameworks (ABMIL, DSMIL, CLAM-SB, CLAM-MB) and compare against modern transformer-based methods (TransMIL, HAG-MIL). They also explicitly compare against alternative multi-scale fusion methods (Concatenation, Cross-Scale Attention). Furthermore, the usage of three state-of-the-art CPath foundation models (CONCH, GigaPath, UNI2) demonstrates robustness. The tuning budgets appear fair, with all models trained under standard cross-entropy / survival losses with equivalent epochs.

### Dataset Assessment
The datasets used are the NIHR BioResource Breast Cancer Dataset (491 cases) and SurGen (425 cases). While these are high-quality, real-world clinical datasets covering important tasks (ER, PR, HER2, and CRC Survival), the absolute number of WSIs (under 1,000 combined) is somewhat small for deep learning in CPath. This small sample size contributes to the high variance seen in the results. Contamination risk is low since the evaluation relies on standard 5-fold cross-validation.

### Metric Assessment
Metrics are appropriate: AUC for binary biomarker classification and C-index for survival prediction. Complementary metrics like F1-score or AUPRC would have been highly beneficial given that biomarker expression (e.g., HER2 positive) can often be imbalanced, but AUC is a standard starting point.

### Statistical Rigor
The authors report standard deviations obtained via 2000 bootstrap trials (Appendix E). This is a strong practice. However, they fail to perform strict statistical significance testing (e.g., paired t-tests or Wilcoxon signed-rank tests) between the baseline models and MSPN. Given that the standard deviations are relatively large (e.g., $\pm 2.0\%$ to $\pm 3.5\%$) and the performance gains are often in the $1.0\%$ to $4.0\%$ range, it is difficult to definitively conclude statistical significance for every task without explicit p-values.

### Ablation Assessment
The ablation study (Table 3) successfully isolates the impact of the number of FOVs (scales). Adding more scales generally improves performance, validating the progressive design. However, a critical ablation is missing: the paper does not isolate the *grid-based remapping* from the *CGN*. What happens if standard multi-scale inputs (actual 5x and 10x features) are fed into the CGN instead of the pseudo-coarse features from grid remapping? This would prove whether grid remapping is merely an efficiency trick or a superior representational choice.

### Missing Experiments
1. **Actual vs. Synthesized Multi-Scale**: An experiment comparing MSPN using actual 10x/5x extracted features versus MSPN using the 20x grid-remapped features.
2. **Pooling Strategy Ablation**: Comparing average pooling in the grid remapping step against max pooling or attention-based pooling.
3. **Statistical Significance Tests**: Explicit p-values for the performance deltas in Table 1.

### Error Analysis Assessment
Significant gaps exist here. The paper provides no systematic error analysis. It lacks an investigation into *when* or *why* the model fails (e.g., does it fail on borderline HER2 2+ cases?). Figure 4 shows qualitative successes, but no failure cases or adversarial examples are discussed.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

5.5


## Significance & Impact
### Impact Assessment

**1. Technical Significance (70%):** 
The technical utility of this paper is substantial for a specific, pragmatic reason: computational and storage bottlenecks in digital pathology. Extracting features from gigapixel WSIs at multiple magnifications (e.g., 20x, 10x, 5x) effectively multiplies the required storage space and inference time by a factor of 1.25x to 2x. By proposing a method that requires only the 20x features to synthesize multi-scale context, MSPN provides a highly attractive drop-in replacement for labs operating under compute or storage constraints. The fact that it readily integrates into existing standard MIL pipelines (CLAM, ABMIL) without architectural overhauls increases its likelihood of adoption. However, it is an engineering optimization rather than a fundamentally new capability. 

**2. Scientific Significance (30%):** 
Scientifically, the contribution is marginal. The paper reinforces the known concept that multi-scale spatial context is beneficial for WSI analysis. It demonstrates that spatial averaging of high-level embeddings can serve as a proxy for lower-magnification fields of view. However, it does not reveal fundamentally new insights into tumor microenvironments, nor does it propose a theoretical framework that shifts how the community understands weakly supervised learning. It is an applied methodology paper that solves an efficiency problem, rather than a discovery paper.

**3. The 3-Year Citation Projection:** 
The paper is likely to receive a moderate number of citations (approximately 20-40 citations per year). Its primary audience will be practitioners and researchers building applied CPath pipelines who want to claim "multi-scale" benefits without paying the computational cost of extracting actual multi-scale features or running complex transformer models like HAG-MIL. It will be cited alongside other efficient MIL aggregation techniques, but it is unlikely to become a foundational citation in the field.

**Impact Score: 5.0 / 10**

5.0


## Scoring Breakdown
- **Novelty:** 4.0
- **Technical Soundness:** 6.5
- **Experimental Rigor:** 5.5
- **Impact:** 5.0

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 5.2
