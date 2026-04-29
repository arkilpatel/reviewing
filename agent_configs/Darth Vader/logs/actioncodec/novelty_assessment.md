### Claimed Contributions
1. Establishing specific design principles for action tokenization focusing on VLA optimization rather than just generative/reconstruction fidelity.
2. Identifying four best practices based on information-theoretic insights: maximized temporal overlap, minimized vocabulary redundancy, enhanced multimodal mutual information, and token independence.
3. Introducing ActionCodec, a high-performance action tokenizer built on these principles, which achieves SOTA results on the LIBERO benchmark using a SmolVLM2-2.2B backbone without robotics pre-training.

### Prior Work Assessment
Action tokenization in VLAs has typically relied on heuristic discretizations (like simple binning) or data-driven methods (VQ-VAEs) that optimize for reconstruction error (e.g., standard VQ-VAE or diffusion-based experts). Previous works like RT-2 and OpenVLA treat tokenization mostly as a preprocessing step for the autoregressive objective. The delta here is conceptually solid: shifting the objective of the tokenizer from 'signal reconstruction' to 'downstream VLA optimization efficiency'. 
The four specific design principles proposed, while individually grounded in standard representation learning (like token independence and mutual information), are combined in a novel context tailored for robotic action chunking.

### Novelty Verdict
Substantial

### Justification
The paper addresses a significant bottleneck in VLA architectures—how the continuous action space is discretized for LLM backbones. While previous works have used VQ-VAEs for this purpose, evaluating and optimizing the tokenizer specifically through the lens of autoregressive training dynamics and information theory is a substantial contribution. It moves beyond naive application of VQ techniques and provides a structured framework for what makes an action token "good" for a VLA.

### Missing References
The paper should ensure a thorough comparison with concurrent tokenizer techniques used in general continuous-to-discrete modalities (e.g., audio/speech tokenizers like EnCodec) to see if these principles are universally applicable or just robotics-specific.

Score: 7.0
