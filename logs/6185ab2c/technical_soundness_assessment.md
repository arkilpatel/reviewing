### Claims Inventory
1. **Conceptual Claim:** There is an inherent text-structure robustness trade-off in TAG learning.
2. **Empirical Claim:** Simple RGNNs (like GNNGuard) achieve competitive robustness when using advanced text encoders.
3. **Empirical Claim:** GraphLLMs are highly vulnerable to training data poisoning compared to GNNs.
4. **Methodological/Empirical Claim:** The proposed SFT-auto framework achieves balanced robustness against both textual and structural attacks.

### Verification Results
1. **Text-structure trade-off (Verified):** The empirical results consistently show structure-oriented models failing under structural attacks but resisting text attacks, and vice-versa for text-oriented models. The reasoning is sound.
2. **Simple RGNNs with advanced encoders (Verified):** The paper provides clear evidence that when decoupled from shallow embeddings, RGNNs perform strongly.
3. **GraphLLM poisoning vulnerability (Verified):** The transductive poisoning results demonstrate significant performance drops for LLM-based methods.
4. **SFT-auto balanced robustness (Verified):** The pipeline (detection followed by adaptive recovery) logically explains how it circumvents the trade-off, and the results back this up.

### Errors and Concerns
- **Concern (Minor):** The complexity analysis states SFT-auto's cost is comparable to SFT-neighbor. While technically true in big-O terms, the worst-case involves two LLM forward passes per sample, which does increase latency. However, this is acknowledged as a small fraction in practice ($p_{attack}$ is small). This is a minor concern and does not undermine the core claims.

### Internal Consistency Check
The claims align perfectly with the empirical results presented in the tables and figures. 

### Theory-Practice Gap Assessment
The paper is primarily empirical. The threat models (GMA, poisoning, evasion) are standard and well-defined, and the experimental setup faithfully executes these attacks.

### Overall Technical Soundness Verdict
Sound. The methodology is clearly described, and the logical chain from empirical observation to the proposed SFT-auto solution is robust.

**Technical Soundness Score: 8.0 / 10**