### Claimed Contributions
1. **Tailored Image Corruptions:** Adapting 20 common image corruptions into time-, stereo-, and depth-consistent perturbations for dense matching.
2. **Corruption Robustness Metric:** A ground-truth-free robustness metric based on Lipschitz continuity to disentangle robustness and accuracy.
3. **Benchmark Functionality:** A public evaluation server and subsampling strategy.
4. **Initial Robustness Evaluation:** Benchmarking 16 state-of-the-art models, revealing severe sensitivities to corruptions.

### Prior Work Assessment
- **Common Corruptions (Hendrycks & Dietterich):** The core idea of 20 image corruptions comes from ImageNet-C. The delta is applying them with multi-frame, stereo, and 3D depth consistency. This is a very non-trivial engineering and conceptual step necessary for tasks like scene flow.
- **Robustness in Optical Flow:** Prior work has focused on adversarial attacks or isolated corruptions (like rain/fog or low light). RobustSpring is the first comprehensive benchmark spanning optical flow, scene flow, and stereo simultaneously.
- **Robustness Metrics:** Adversarial robustness metrics in flow have been studied, but adapting a Lipschitz-based metric for unoptimized generic corruptions, specifically without ground truth (to separate accuracy from robustness), is a clean conceptual advancement.

### Novelty Verdict
Substantial. While the concept of benchmarking common corruptions is well-known in image classification (ImageNet-C), translating this meaningfully to dense 3D matching over time is highly non-trivial and represents a substantial artifact and methodological contribution.

### Justification
The engineering effort required to ensure that a snowflake or fog behaves consistently across a stereo baseline and over multiple frames is significant. It prevents the benchmark from being artificially easy or breaking geometric constraints that scene flow algorithms rely on.

### Missing References
None identified. The paper comprehensively cites relevant literature on dense matching, benchmarks, and robustness.