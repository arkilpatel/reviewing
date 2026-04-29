# Final Review: VEQ: Modality-Adaptive Quantization for MoE Vision-Language Models

This paper proposes Visual Expert Quantization (VEQ), a Post-Training Quantization (PTQ) framework specifically designed for Mixture-of-Experts (MoE) Vision-Language Models (VLMs). The authors identify that standard PTQ paradigms fail to account for two distinct forms of heterogeneity within these architectures: the differing activation characteristics between vision and language tokens, and the non-uniform importance of different routing experts. VEQ mitigates these issues through Modality-expert-aware Quantization (scaling errors based on expert activation frequency) and Modality-affinity-aware Quantization (enhancing the Hessian calibration matrix by incorporating token-expert affinity). The method demonstrates significant improvements of ~2-3% accuracy at the challenging W3A16 precision level on modern models like Kimi-VL and Qwen3-VL.

### Novelty
The paper presents a moderate, yet highly logical, methodological novelty. While PTQ for standard LLMs (e.g., GPTQ, AWQ) and dense VLMs is well-explored, the intersection of PTQ with MoE-based VLMs introduces unique structural challenges. The proposed solutions—re-weighting based on expert frequency and modifying the Hessian matrix using token-expert affinity—are sensible adaptations of existing quantization techniques to the MoE domain. The explicit consideration of how different modalities (visual vs. text tokens) route through experts differently is a clever engineering adaptation, representing an expected but highly useful extension of current quantization literature.

### Technical Soundness
The technical approach is fundamentally sound. The underlying premise—that visual and text tokens exhibit divergent activation ranges and routing behaviors, thereby requiring modality-aware calibration—is correct. Constructing an enhanced Hessian matrix by weighting according to token-expert affinity makes mathematical sense within the GPTQ framework, as it prioritizes the preservation of weights most critical to the dominant tokens for a given expert. The only minor technical concern is the potential risk of the Hessian overfitting to the specific modality ratio of the calibration dataset; careful balancing of text and image tokens during calibration is necessary to prevent severe degradation in visual pathways. 

### Experimental Rigor
The experimental evaluation is mostly rigorous and targets the highly relevant W3A16 (3-bit weight) configuration, which is notoriously difficult for multimodal models. Achieving a +2.04% gain on Kimi-VL and +3.09% on Qwen3-VL over existing state-of-the-art baselines is a compelling result. However, the evaluation has a few notable gaps. Given the sensitivity of Hessian-based PTQ to the calibration dataset, the paper must report variance across different random samples of the calibration set to prove the robustness of the constructed Hessian. Furthermore, an explicit sensitivity analysis on the calibration dataset's modality ratio (e.g., performance when calibrating on 90% text vs. 50/50 text/image) is crucial to fully validate the "modality-aware" claims. Finally, the ablation study must clearly isolate the individual contributions of the expert-aware scaling versus the affinity-aware Hessian modification.

### Impact
The real-world utility of this paper is extremely high. MoE VLMs are massively computationally expensive, making effective PTQ mandatory for deployment on consumer hardware or constrained edge devices. Providing a robust W3A16 quantization scheme that restores significant accuracy translates directly to massive cost savings in serving infrastructure. While specific PTQ heuristics often have a limited lifespan as underlying architectures evolve, the core insight of requiring modality-aware calibration for sparse multimodal models is scientifically valuable and will be highly relevant to the systems and deployment communities over the next few years.

### Scoring Breakdown
- **Impact:** 7.5 / 10
- **Technical Soundness:** 8.0 / 10
- **Experimental Rigor:** 7.0 / 10
- **Novelty:** 6.0 / 10

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Calculation:** `(4.0 * 7.5 + 2.0 * 8.0 + 2.0 * 7.0 + 2.0 * 6.0) / 10 = (30.0 + 16.0 + 14.0 + 12.0) / 10 = 7.2`
**Final Score:** 7.2
