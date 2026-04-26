### Claimed Contributions
1. Formulation of Anchored E-Watermarking: using e-values instead of p-values to allow for anytime-valid early stopping in statistical watermarking.
2. Derivation of the robust log-optimal e-value and the worst-case optimal log-growth rate $J^*$ for target distributions within a $\delta$-neighborhood of an anchor distribution $p_0$.
3. Theoretical bounds on the expected stopping time (sample complexity) for this sequential testing framework.

### Prior Work Assessment
- **Speculative decoding and anchor models for watermarking**: The use of an auxiliary open-source anchor model and speculative decoding to embed watermarks was recently introduced by SEAL (Huang et al., 2025). The proposed generation coupling $w^*$ is identical to SEAL. The delta here is solely on the detector side (using e-values instead of fixed-horizon p-values).
- **Sequential testing and e-values**: The use of e-values and test martingales for anytime-valid testing is a well-established statistical framework (Vovk, Ramdas, Grunwald).
- **Delta**: The paper merges these two distinct lines of work by applying the standard e-value framework (robust log-optimality) to the anchor-based watermarking setting of SEAL. While useful, this is a relatively predictable combination.

### Novelty Verdict
Moderate

### Justification
The paper does not introduce a fundamentally new watermarking paradigm. The generator mechanism is identical to prior work (SEAL). The novelty lies entirely in framing the detection problem as a sequential test using e-values, which is a standard statistical tool being applied to a new domain. While the derivation of the optimal e-value for this specific $\delta$-neighborhood is mathematically neat, the conceptual leap from existing anchor-based watermarking and sequential testing literature is relatively moderate.

### Missing References
The related work section provides a good overview of both the watermarking and e-value literature. No major omissions were identified.

Score: 5.0