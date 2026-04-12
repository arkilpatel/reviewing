### Claims Inventory
1. Theoretical: The optimal deferral rule for a speculative cascade minimizes the expected loss penalized by the TV distance between drafter and verifier distributions (Lemma 4).
2. Theoretical: Lossy speculative decoding (Tran-Thien, 2023) is a special case of general target distribution speculative sampling (Lemma 2).
3. Empirical: Speculative cascades offer better cost-quality trade-offs than standard cascades and speculative decoding.
4. Conceptual: Token-level cascaded deferral rules can be implemented via target distributions in speculative sampling.

### Verification Results
- Lemma 4: Verified. The derivation follows standard expected loss minimization for a binary decision rule and the known rejection rate of speculative sampling (Lemma 3).
- Lemma 2: Verified. The authors accurately map the acceptance criteria and residual distributions of Tran-Thien (2023) to their target distribution formulation.
- Empirical Claims: Verified via results on WMT, XSum, CNNDM, GSM8K, etc.
- Conceptual Claims: Verified. Formulating target distribution as a linear combination of `q` and `p` weighted by the binary deferral rule is a valid way to leverage speculative execution machinery.

### Errors and Concerns
None of critical or significant severity. The proofs are mathematically sound and borrow safely from established mechanics of speculative sampling. 
Minor Concern: In Lemma 5, the regret bound heavily relies on how well individual models approximate the data generating distribution, which can be a weak bound in practice if both models are poorly calibrated. However, the theoretical derivation is correct.

### Internal Consistency Check
Consistent. The deferral rules evaluated empirically map cleanly back to the target distribution framework proposed in Section 4.

### Theory-Practice Gap Assessment
The optimal rule requires expected losses against the true data-generating distribution `P`. The authors use a plug-in estimator replacing expectations with the model's max probabilities. This introduces a gap, as models are often overconfident or poorly calibrated. The authors acknowledge this and propose token-specific deferral rules (TokenV1-V3) as heuristics to bridge the gap, which empirically perform better.

### Overall Technical Soundness Verdict
Sound.