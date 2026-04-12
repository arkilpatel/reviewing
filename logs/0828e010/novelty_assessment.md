### Claimed Contributions
1. A post-hoc parameter merge method called Neon (Negative Extrapolation from self-traiNing) that improves generative models using self-generated data without needing additional real data or architectural changes.
2. Theoretical proof that mode-seeking inference samplers create a predictable anti-alignment between synthetic and real-data population gradients, thus justifying why negative extrapolation works.
3. Empirical demonstration of Neon's universality across diverse model families (Diffusion, Flow Matching, Autoregressive, Few-step) and datasets, achieving state-of-the-art results (e.g., FID 1.02 on ImageNet 256x256 with xAR-L) using minimal compute overhead (<1%).
4. Empirical demonstration that Neon redistributes probability mass from over-represented to under-represented modes (precision-recall trade-off).

### Prior Work Assessment
- **Synthetic Data Augmentation / Self-Training**: Prior works (Alemohammad et al., 2024a; Shumailov et al., 2024) observed Model Autophagy Disorder (MAD) or model collapse when fine-tuning on self-generated data. Neon flips this narrative by viewing the degradation direction as a useful anti-aligned signal. The closest prior work utilizing degradation is SIMS (Alemohammad et al., 2024b), which uses self-generated data as negative guidance at inference time. However, SIMS requires inference-time modifications and is limited to diffusion models. Neon applies a post-hoc parameter space extrapolation, completely removing inference overhead and applying across all generative model classes.
- **Model Merging/Extrapolation**: Interpolation and extrapolation of weights have been used in task vectors and model averaging (e.g., Ilharco et al., 2022, not cited but conceptually similar in parameter math). However, defining a task vector as the degradation from self-training and extrapolating backwards to improve the base generation capability is conceptually new and clever.
- **DDO (Zheng et al., 2025)**: Formulates models as implicit discriminators, providing gains for likelihood-based models, but does not apply to likelihood-free models like IMM. Neon operates directly on the parameter updates via standard training objectives, agnostic to the objective type.

The delta here is Substantial to Transformative. SIMS used negative guidance during inference, which is costly and architecture-specific. Neon shifts the correction to the parameter space *after* a brief fine-tuning phase, yielding a universal, zero-inference-overhead plug-and-play technique. The theoretical framing of mode-seeking samplers inducing anti-aligned gradients provides strong foundational backing.

### Novelty Verdict
Substantial

### Justification
The technique itself (linear extrapolation of parameters) is mathematically simple, but the application—purposely degrading a model on its own data to discover an anti-aligned vector against the population gradient—is highly creative and impactful. It solves the inference overhead problem of SIMS and the architecture restrictions of DDO. The theoretical characterization of this mechanism (linking sampler mode-seeking bias to gradient anti-alignment) is a significant conceptual contribution.

### Missing References
While the authors cite relevant model collapse literature, referencing generic "task arithmetic" or weight interpolation literature (e.g., "Editing Models with Task Arithmetic", Ilharco et al., 2023) might enrich the context, though it's not strictly a missing baseline for generative synthetic self-training. The paper accurately compares itself to the most relevant recent methods (SIMS, DDO, Discriminator Guidance).
