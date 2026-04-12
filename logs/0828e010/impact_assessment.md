### Impact Assessment
**1. Technical Significance (70%):**
Neon provides an extraordinarily high degree of technical utility. The generation of high-quality image data is often bottlenecked by real data availability and the massive computational cost of generative training. Neon offers a "free lunch" mechanism: it uses negligible additional compute (<1% of the base model's training budget), requires no new real data, and applies seamlessly across architectures (diffusion, flow matching, autoregressive, and few-step models) as a simple post-hoc parameter merge. Its ability to elevate state-of-the-art models (like xAR-L) to a new record FID of 1.02 on ImageNet-256 without inference overhead makes it highly likely to see widespread, immediate adoption by practitioners seeking to squeeze the last bit of performance out of strong foundation models.

**2. Scientific Significance (30%):**
Scientifically, the paper flips the prevailing narrative of "Model Autophagy Disorder" (MAD). Rather than viewing degradation from synthetic self-training as a catastrophic failure mode to be avoided, Neon demonstrates mathematically and empirically that this degradation is a highly structured, anti-aligned signal. The authors provide a formal framework characterizing how mode-seeking samplers induce this anti-alignment. This insight changes how the community understands self-training dynamics and establishes a new link between inference-time sampler biases and parameter-space gradient alignment.

**3. The 3-Year Citation Projection:**
This paper is highly likely to receive widespread citations in the next 3 years. The technique is simple enough to be adopted as a standard post-processing step in the release cycle of major generative models. Researchers studying synthetic data augmentation, model collapse, and task arithmetic will cite this work heavily for its theoretical and empirical reframing of synthetic data degradation.

**Impact Score: 9.5 / 10**