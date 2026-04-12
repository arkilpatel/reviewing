### Claims-to-Experiments Mapping
- Claim 1: VLMs struggle with SMM. Supported by Table 1 (17 models tested).
- Claim 2: Scaffolds without training don't help much. Supported by Table 3.
- Claim 3: Map-then-reason SFT is best. Supported by Table 4.
- Claim 4: RL needs SFT. Supported by Table 4.
- Claim 5: LLM is the bottleneck. Supported by Table 12.

### Baseline Assessment
Appropriate and strong. The paper evaluates 17 SOTA open and closed-source models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Qwen2.5-VL, DeepSeek-VL2). For the training experiments, the baselines (Raw-QA, FFR alone, Map alone) are well-designed to isolate the contribution of the proposed joint map-and-reason approach.

### Dataset Assessment
MINDCUBE (21k questions, 3.2k images) covers Rotation, Among, and Around settings. It uses established datasets (ArkitScenes, WildRGB-D) and self-collected data. The dataset is sufficiently challenging (best zero-shot open model is ~47%). Data contamination is unlikely to be an issue for the specific spatial reasoning queries generated via templates.

### Metric Assessment
Appropriate. QA accuracy is standard. The graph metrics (Overall Similarity, Isomorphic Rate) for the generated cognitive maps are custom but well-defined mathematically (Section D.2) to handle rotation invariance.

### Statistical Rigor
- **Variance reporting:** Missing. The paper does not report error bars, standard deviations, or multiple random seeds for the SFT and RL training runs. Given the noise often associated with RL fine-tuning (GRPO), this is a significant gap.
- **Number of runs:** Appears to be single runs for the main training results. 
- **Statistical significance:** Not tested.

### Ablation Assessment
Excellent. The paper systematically ablates the input/output structures (Raw, Map-In, Map-Out, FFR, Map+FFR) and the training phases (Zero-shot, SFT, RL from scratch, RL from SFT). It also ablates the vision encoder vs. LLM tuning (Table 12) and the RL reward structure (Table 18).

### Missing Experiments
- Reporting variance/seeds for the RL experiments.

### Error Analysis Assessment
The paper includes a failure case analysis (Section C.6 and Appendix) showing that models rely on local matching.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps. The ablation design is incredibly thorough and well-thought-out, but the lack of variance reporting for RL training is a standard flaw.