### Claimed Contributions
1. Identifying two forms of heterogeneity in MoE VLMs that standard Post-Training Quantization (PTQ) ignores: discrepancy between vision/language tokens and non-uniform expert contributions.
2. Proposing Visual Expert Quantization (VEQ), which utilizes Modality-expert-aware Quantization (prioritizing pivotal experts using activation frequency) and Modality-affinity-aware Quantization (enhancing the Hessian matrix with token-expert affinity).
3. Demonstrating SOTA PTQ performance on Kimi-VL and Qwen3-VL in W3A16 configurations.

### Prior Work Assessment
PTQ for LLMs (like GPTQ, AWQ, SmoothQuant) is well-established. PTQ for MoE architectures (like MoEQ) and standard VLMs (like LLaVA-PTQ) are also active research areas. The delta here lies in the intersection: PTQ specifically for *MoE-based VLMs*. 
While re-weighting quantization error based on expert activation frequency is a known trick in dense-to-sparse or standard MoE quantization, combining it with a modality-aware Hessian calibration matrix that factors in token-expert affinity is a logical, yet reasonably novel, structural adaptation. It specifically accounts for how visual tokens route differently than text tokens within the MoE layers.

### Novelty Verdict
Moderate

### Justification
The paper combines existing concepts (PTQ, Hessian-based calibration, expert routing frequencies) and applies them to a relatively new, highly specific architectural combination (MoE + VLM). While the "Modality-affinity-aware" Hessian modification is a clever engineering adaptation, it fundamentally relies on established GPTQ-style paradigms. It represents a sensible and expected extension of the quantization literature into the MoE-VLM domain rather than a transformative paradigm shift.

### Missing References
The paper should ensure adequate comparison with recent MoE-specific quantization schemes (e.g., QMoE) and VLM-specific schemes to isolate whether the "modality-awareness" actually provides the lift, or if standard MoE quantization works just as well.

Score: 6.0
