### Claimed Contributions
1. **Tailored image corruptions:** A new dataset (RobustSpring) introducing 20 corruptions for optical flow, scene flow, and stereo, with time, stereo, and depth consistency.
2. **Corruption robustness metric:** A metric based on Lipschitz continuity that compares the difference between clean and corrupted predictions, disentangling robustness from accuracy.
3. **Benchmark functionality:** A standardized public benchmark evaluating dense matching models.
4. **Initial robustness evaluation:** Benchmarking of 16 models across the three tasks, revealing varying sensitivities to different corruptions.

### Prior Work Assessment
- **Common Corruptions:** Hendrycks & Dietterich (2019) introduced the 15+ common corruptions for 2D images.
- **Corruptions for Optical Flow:** Yi et al. [78] (2024) benchmarked optical flow robustness to corruptions. RobustSpring's delta is extending this to scene flow and stereo, and critically, introducing the temporal, stereo, and depth consistency rendering required for 3D/video tasks.
- **Robustness metrics:** Previous works on adversarial robustness for optical flow (e.g., Schmalfuss et al., 2022) used the difference between clean and corrupted predictions. RobustSpring adapts this to non-adversarial common corruptions.
- **Spring Dataset:** Mehl et al. (2023) introduced the high-resolution Spring dataset. RobustSpring directly builds on it.

### Novelty Verdict
**Substantial**

### Justification
While applying common corruptions to new domains is a common paradigm, doing so naively for stereo videos breaks geometric and temporal consistency. The authors carefully engineer corruptions (like fog, rain, snow, motion blur) to be coherent across the temporal and stereo dimensions and the 3D depth of the scene. This is a non-trivial and necessary contribution for evaluating dense matching. Furthermore, the creation of the first unified robustness benchmark spanning all three tasks (optical flow, scene flow, stereo) is a substantial artifact contribution.

### Missing References
The related work section is quite comprehensive, properly citing the Spring dataset, prior adversarial and corruption works in optical flow, and foundational 2D corruption benchmarks. No major missing references are apparent.