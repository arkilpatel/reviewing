### Claims Inventory
1. **Theoretical**: The AM-$\mu$P maximal-update learning rate scales as $\Theta(L_{tr}^{-3/2})$ for Transformers (Proposition 3.5).
2. **Conceptual**: AM-$\mu$P provides a robust, network-wide budget for update magnitudes.
3. **Empirical**: The derived depth-scaling exponent of -1.5 holds empirically across architectures.

### Verification Results
1. **Transformer Depth Scaling Proof**: Significant Error / Theory-Practice Gap
2. **AM-$\mu$P Derivation**: Verified
3. **Empirical Consistency**: Error Found (Significant deviation for Adam and Post-LN Transformers)

### Errors and Concerns
- **Critical Theory-Practice Gap in Transformers (Significant Error)**: In Appendix D, the proof for Transformers relies on Assumption 1 and the explicit assumption that the pre-LayerNorm sum $u^{(l)}$ satisfies $s(u^{(l)}) = \Theta(1)$ independent of $L_{tr}$ (Line 1083). However, the authors explicitly state in Section 3.1 (Line 316) that they use standard fan-in initialization for Transformer sublayers. Without explicitly scaling down the residual branches by $1/\sqrt{L_{tr}}$ (which they do for ResNets but omit for Transformers), the variance of the pre-LN sum $u^{(l)}$ grows linearly with depth $l$ in post-norm Transformers. Consequently, $s(u^{(l)})$ scales as $\sqrt{l}$, which violates the $\Theta(1)$ assumption. If $s(u^{(l)}) \propto \sqrt{l}$, the LayerNorm Jacobian's operator norm shrinks as $1/\sqrt{l}$, which alters the overlap propagation in Eq. 42 and invalidates the $-3/2$ exponent derivation. 
- **Inconsistency with Empirical Results**: The empirical results for Post-LN ViT on ImageNet yield an exponent of -1.178, which is far from the theoretical -1.5. This 21.5% deviation is likely a direct consequence of the aforementioned theoretical flaw. Furthermore, when using the Adam optimizer, the exponents shift significantly to -1.207 for CNNs and -1.269 for ResNets. In logarithmic space, a 20% shift in the exponent causes massive deviations at scale, contradicting the claim that these are merely "secondary modulations."

### Internal Consistency Check
The paper claims a universal -3/2 power law, but the ablation studies (Table 3) show exponents ranging from -1.131 to -1.701. The authors claim this is "strong agreement," but an exponent of -1.131 means the learning rate decays much slower than $L^{-1.5}$, which is inconsistent with the central claim of universality.

### Theory-Practice Gap Assessment
The theory heavily assumes MSE loss and SGD at initialization. While MSE is a standard theoretical surrogate, the reliance on SGD without momentum completely ignores the reality of modern training (Adam/AdamW). The empirical results show that Adam fundamentally alters the scaling exponent, breaking the theory-practice translation.

### Overall Technical Soundness Verdict
Significant concerns

Score: 3.5 / 10