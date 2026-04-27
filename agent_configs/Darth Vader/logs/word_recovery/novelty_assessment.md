### Claimed Contributions
The paper claims to explain the recently observed phenomenon of large language models' robustness to character-level tokenization. The authors introduce a "word recovery" concept, where models reconstruct canonical word-level tokens from character inputs. They propose a decoding-based method using the output embedding matrix to detect this recovery, a subspace intervention to prove its causal necessity, and an attention masking technique to show the reliance on in-group attention in early layers.

### Prior Work Assessment
The behavioral observation that LLMs are robust to non-canonical, character-level tokenization without fine-tuning was already established by Zheng et al. (2025). Furthermore, the notion that models build internal word-level representations or lexicons has been widely explored (e.g., Feucht et al., 2024; Kaplan et al., 2025; Kaushal & Mahowald, 2022). The interpretability techniques employed—Logit Lens (Nostalgebraist, 2020), targeted subspace removal (Meng et al., 2022), and attention masking—are entirely standard in the mechanistic interpretability literature. 

### Novelty Verdict
The paper's primary contribution is connecting existing behavioral findings (Zheng et al., 2025) with standard mechanistic interpretability probing. While this specific application is somewhat novel, it is a highly incremental step. The paper does not introduce new interpretability primitives or discover a fundamentally surprising mechanism, as the aggregation of characters into token-like representations is the most intuitive hypothesis for character-level robustness.

### Justification
Given the extensive prior work on tokenization robustness and implicit internal lexicons, merely applying standard probing techniques to confirm the most obvious hypothesis yields limited novelty. The work is derivative of recent behavioral papers.

### Missing References
The authors have adequately cited recent work like Zheng et al. (2025) and Kaplan et al. (2025), but they overstate the novelty of their mechanistic findings in light of these papers.

Score: 4