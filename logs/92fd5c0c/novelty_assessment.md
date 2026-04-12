### Claimed Contributions
1. Formalizes the problem setting of model routing with a dynamic pool of LLMs.
2. Proposes UniRoute, a routing approach relying on an LLM feature representation based on its prediction error vector on a set of representative prompts.
3. Proposes two instantiations based on unsupervised or supervised clustering.

### Prior Work Assessment
The paper claims existing works focus on static routing (fixed pool). However, due to the completely broken bibliography (e.g., `[???]`), it is impossible to properly verify the delta against the specific prior works they intended to cite. However, representing an expert by its prediction signature on a validation set is a known technique in ensemble learning, though its application to dynamic LLM routing is a solid, useful extension.

### Novelty Verdict
Substantial. The application to dynamic LLMs and the cluster-based risk bounds provide a meaningful delta over static routing.

### Justification
Despite the missing bibliography, the core idea of using a validation-set error vector as a dense representation of an LLM for zero-shot routing is a creative and highly practical framing of the problem.

### Missing References
The entire bibliography is missing!
