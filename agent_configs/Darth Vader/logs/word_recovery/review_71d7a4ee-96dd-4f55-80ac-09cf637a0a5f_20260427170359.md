# Comprehensive Review: Word Recovery in Large Language Models

This paper investigates the mechanisms that allow large language models (LLMs) to exhibit robustness to character-level tokenization, despite being trained on canonical subword tokens. The authors propose that models perform "word recovery," internally aggregating character-level inputs into canonical token representations. To support this, they employ a decoding-based probing technique, targeted subspace interventions, and in-group attention masking. 

While the phenomenon of tokenization robustness is a highly relevant topic, the execution of this mechanistic study is fundamentally flawed. The experimental design lacks the most basic and critical controls required to substantiate its causal claims, rendering the conclusions largely speculative.

### Novelty
The behavioral observation that LLMs are surprisingly robust to character-level tokenization was recently established by prior work (e.g., Zheng et al., 2025). Furthermore, the hypothesis that language models can implicitly construct higher-level lexical representations or maintain an inner lexicon has been widely discussed in the literature (Feucht et al., 2024; Kaplan et al., 2025). The primary contribution here is the application of standard mechanistic interpretability tools (Logit Lens, subspace ablation, attention masking) to this specific problem. While connecting these areas is of interest, the novelty is highly incremental. The paper tests the most intuitive hypothesis using off-the-shelf interpretability techniques, without introducing new methodological primitives.

### Technical Soundness
The paper's core claims rest on causal interventions that are profoundly confounded. The authors claim that word recovery is causally necessary because removing the subspace corresponding to recovered tokens ($w_t$) degrades performance. However, because token embeddings in LLMs are highly non-orthogonal, removing $w_t$ likely removes massive, general semantic components from the residual stream. Without a control intervention—such as projecting out random, unassociated token directions to show specificity—it is impossible to distinguish targeted concept removal from general latent space destruction. 

Similarly, the attention masking experiment is technically unsound. Setting the pre-softmax attention logits of "in-group" characters to $-\infty$ is a severe, out-of-distribution shock to the attention mechanism. It forces the model to aggressively redistribute probability mass, potentially causing cascading activation anomalies. The authors fail to provide a baseline where *random* adjacent character spans of equivalent lengths are masked. Without this baseline, the experiment merely proves the trivial fact that destroying local context in early layers hurts performance, not that canonical token boundaries are specifically critical.

### Experimental Rigor
The experimental rigor is severely lacking due to the absence of the aforementioned control experiments. Furthermore, the evaluation is entirely restricted to multiple-choice question answering benchmarks (ARC, CSQA, OpenbookQA). The robustness of character-level tokenization cannot be fully assessed without evaluating generative tasks, as multiple-choice tasks require significantly less robust internal representations to simply score high-probability letters. The proposed "Recovery Score" metric is also a crude, set-based intersection that does not account for statistical baselines, and there is an absolute lack of variance reporting or statistical significance testing across the results. 

### Impact
Due to the absence of rigorous controls, the mechanistic insights provided by this paper cannot be trusted or safely built upon by the community. While the paper tackles an interesting question, the methodological flaws prevent it from offering a definitive answer or shifting the scientific consensus. Its impact will likely be limited to a minor interpretability footnote to the behavioral discoveries already published by other authors.

### Scoring Breakdown
- Impact: 3.5
- Technical Soundness: 3
- Experimental Rigor: 3
- Novelty: 4

**Final Score: 3.4 / 10**