### Claims-to-Experiments Mapping
- **Claim: Local geometry is better than global geometry for memory conditioning.** Supported by the ablation study explicitly comparing global vs. local 3D memory.
- **Claim: Multi-anchor weaving with pose-guided fusion is necessary.** Supported by the ablation study showing artifacts when using average fusion versus pose-guided weighted sum.
- **Claim: AnchorWeave achieves SOTA long-horizon consistency.** Supported by comparisons against ViewCrafter, TrajCrafter, Gen3C, EPiC, SEVA, Context-as-Memory, and SPMem under partial-revisit and free-form trajectory settings.

### Baseline Assessment
The baseline selection is excellent and comprehensive. It includes the absolute latest concurrent work (2024 and 2025 papers) covering diverse paradigms: single-image control (ViewCrafter, Gen3C, TrajCrafter, EPiC), implicit multi-view history (Context-as-Memory, SEVA), and global 3D memory (SPMem). For the closed-source baselines (Context-as-Memory, SPMem), the authors reimplemented them on the exact same backbone (CogVideoX) using the same training data, ensuring a highly fair comparison. 

### Dataset Assessment
The paper uses RealEstate10K and DL3DV, which are standard, large-scale, and diverse datasets for 3D/video generation tasks. Testing on a subset of 500 videos for the partial-revisit evaluation is a reasonable scale. Furthermore, the inclusion of a zero-shot third-person dynamic game environment evaluation (despite training only on static scenes) strongly demonstrates the generalizability of the method.

### Metric Assessment
The quantitative metrics (PSNR, SSIM, LPIPS for quality/consistency) and camera control metrics (Rotation Error, Translation Error) are standard and appropriate for the task. The paper utilizes the evaluation protocols of recent work (like EPiC), making the results contextualized.

### Statistical Rigor
**Gap**: Like many generative modeling papers, there is a lack of statistical variance reporting. The quantitative tables report single point estimates without standard deviations, confidence intervals, or indications of how many random seeds were used for the generation process. In highly stochastic diffusion models, variance over multiple seeds is important. 

### Ablation Assessment
The ablation studies are thorough and isolate the key contributions perfectly:
1. Global vs. Local 3D Memory
2. Average vs. Pose-conditioned Fusion
3. Joint vs. Separate Attention
4. Number of retrieved anchors ($K=1$ to $K=4$).
These experiments directly validate the core design choices of the paper.

### Missing Experiments
- **Computational Cost / Latency Analysis**: Since the method requires rendering multiple local point clouds and evaluating coverage during generation, an analysis of the inference time compared to global memory approaches (which only need to render one scene) is missing and highly relevant.
- **Failure Cases**: A dedicated section analyzing where the multi-anchor weaving fails (e.g., highly reflective surfaces, extreme depth estimation failures) would improve the rigor.

### Error Analysis Assessment
The paper includes some qualitative discussion of why baselines fail (e.g., hallucinations due to global drift), but lacks a rigorous categorization or quantitative breakdown of its own failure modes.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

### Score
6.5
