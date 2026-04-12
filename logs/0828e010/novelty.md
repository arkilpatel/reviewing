### Claimed Contributions
1. Introduction of Neon, a post-hoc method that improves generative models by fine-tuning on self-generated data and then performing negative extrapolation on the weights.
2. A theoretical proof that mode-seeking samplers create an anti-alignment between synthetic and real-data gradients, explaining why Neon works.
3. Demonstration of Neon's universality and efficiency across multiple state-of-the-art architectures with <1% overhead.
4. Analysis showing Neon operates via a precision-recall trade-off.

### Prior Work Assessment
- **Self-training and Model Collapse:** The phenomenon of MADness or model collapse is well-documented (Shumailov et al., 2024; Alemohammad et al., 2024a). This paper flips the problem on its head by utilizing the collapse direction as a negative signal.
- **Improving with Synthetic Data:** Prior works like Discriminator Guidance (Kim et al., 2023a), SIMS (Alemohammad et al., 2024b), and DDO (Zheng et al., 2025) have used synthetic data. However, SIMS requires negative guidance during inference (increasing cost), and DDO formulates implicit discriminators (limited to likelihood-based models). 
- **Delta:** Neon is transformative in its simplicity. Instead of modifying the inference procedure or adding auxiliary networks, it performs a one-time parameter space extrapolation. The theoretical link connecting sampler bias to gradient anti-alignment is highly original.

### Novelty Verdict
Substantial to Transformative. The idea of negative weight extrapolation after self-training to reverse model collapse is elegant, conceptually novel, and distinct from existing synthetic data augmentation techniques.

### Justification
The contribution is not just empirical; the mathematical formalization of why the degradation direction is anti-aligned with the true improvement direction provides a fresh perspective on generative model training dynamics.

### Missing References
None identified. The paper adequately cites recent and relevant work on model collapse and synthetic data augmentation.

**Novelty Score: 8.5 / 10**