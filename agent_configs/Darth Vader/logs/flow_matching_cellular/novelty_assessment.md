### Claimed Contributions
1. A theoretical decomposition of virtual screening error into generative modeling error and perturbation representation error.
2. An extensive empirical ablation of flow matching design choices for microscopy, showing that standard Noise-to-Data (N->D) flows outperform domain-specific Control-to-Perturbed (C->P) flows and optimal transport couplings.
3. A simple, stable, scalable architecture (Microscopy Transformer - MiT) achieving state-of-the-art FID/KID on RxRx1 and BBBC021.
4. Using MolGPS (a pretrained graph transformer) for conditioning on unseen molecules, improving zero-shot generation of cell phenotypes under new chemical perturbations.

### Prior Work Assessment
- The theoretical error decomposition is a straightforward application of the triangle inequality on distribution distances, conceptually similar to domain adaptation bounds.
- The empirical ablation borrows heavily from Karras et al. (2022) and Peebles & Xie (2023) but applies it to the cellular microscopy domain. Prior works like CellFlux (Zhang et al., 2025) proposed complex C->P flows. The delta here is demonstrating that standard methods work better when properly tuned and scaled.
- The architecture (MiT) is a slight modification of Diffusion Transformers (DiT) with long-range skip connections and RMSNorm.
- Using MolGPS instead of Morgan Fingerprints is a sensible but predictable combination of recent representation learning advances with generative modeling.

### Novelty Verdict
Moderate

### Justification
The paper's primary contribution is empirical and corrective. It does not introduce a fundamentally new paradigm or algorithm; rather, it systematically strips away unnecessary domain-specific complexity introduced by prior works (like CellFlux) and replaces it with well-established scalable generative modeling techniques (N->D flows, DiT). The insight that standard methods, when scaled and stabilized, outperform specialized ones is highly valuable but conceptually moderate. The use of MolGPS is a solid application of existing tools. Overall, it's a very well-executed "elucidating the design space" paper, but the methodological novelty is incremental.

### Missing References
None glaringly obvious. The paper appropriately cites the most relevant concurrent and recent works in generative microscopy (CellFlux, CellFluxV2) and diffusion models.

Score: 5.0 / 10
