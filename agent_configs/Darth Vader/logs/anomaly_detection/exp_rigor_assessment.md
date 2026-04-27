# Experimental Rigor Assessment - "Is Training Necessary for Anomaly Detection?"

The paper follows a highly rigorous experimental protocol across multiple benchmarks and settings.

### Strengths:
1. **Comprehensive Benchmarking:** The authors evaluate RAD on four major datasets: MVTec-AD, VisA, Real-IAD, and 3D-ADAM. This covers a wide range of scenarios, from controlled lab images to large-scale real production and 3D manufacturing data.
2. **Standard MUAD and Few-Shot Settings:** Evaluation across both the standard multi-class setting and the few-shot (1, 2, 4-shot) setting demonstrates the versatility of the method.
3. **Multiple Metrics:** The use of 7 metrics (AUROC, AP, F1-max for both image and pixel levels, plus AUPRO) ensures a thorough assessment of both detection and localization capabilities.
4. **Baselines:** Comparison against a wide array of SOTA baselines (reconstruction, distillation, diffusion, embedding-based) is comprehensive. Specifically, comparing against Dinomaly (the current SOTA) is critical.
5. **Ablation Studies:** The ablation of multi-layer memory, global context retrieval, and spatial conditioning (Table A1) clearly quantifies the contribution of each component.
6. **Data Scaling Analysis:** The three scaling settings (single-class, multi-class, incremental-class) provide deep insight into the method's behavior under cold-start and data-scarce conditions. This is a very thorough way to investigate "training-free" claims.
7. **Encoder and Resolution Impact:** Analyzing how RAD scales with stronger encoders (DINOv3 vs others) and higher resolution (224 vs 448) is excellent for future-proofing the method.

### Weaknesses/Caveats:
1. **Reproducibility:** While the paper mentions "Code available at [URL]", the URL in the text is often a placeholder during review. However, the implementation details (ViT-B/16, specific layers, hyperparams) are detailed enough for reproduction.
2. **3D-ADAM Modality:** The 3D-ADAM evaluation uses only the RGB modality. While they acknowledge this as a limitation, a comparison using full 3D signals (if available for baselines) would have been even stronger.

### Assessment:
The experimental rigor is exemplary. The data scaling and cold-start analyses go above and beyond the typical AD paper. The results are consistent across multiple benchmarks and settings, leaving little doubt about the method's effectiveness.

**Score Recommendation (Experimental Rigor): 9.5/10** (Extremely thorough evaluation across multiple dimensions).