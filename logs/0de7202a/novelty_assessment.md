### Claimed Contributions
1. **miniCTX Benchmark**: A Lean 4 benchmark evaluating theorem proving in real-world settings where proofs depend on in-file definitions and long contexts, rather than isolated problems.
2. **NTP-TOOLKIT**: A tool for extracting data from Lean projects to dynamically update the benchmark and avoid training data contamination (temporal split).
3. **File-Tuning Baseline**: A method of fine-tuning language models using full file context and proof states, rather than just proof states.

### Prior Work Assessment
- **miniF2F / ProofNet**: Evaluate on isolated math competition problems. Delta: Substantial. miniCTX focuses on complex, multi-dependency real-world formalization.
- **LeanDojo**: Retrieves premises from Mathlib. Delta: Substantial. LeanDojo operates mainly on static Mathlib (high contamination risk) and focuses on premise retrieval, not raw in-file context (comments, proofs).
- **Baldur**: Uses file context for whole-proof generation. Delta: Moderate. File-tuning is a straightforward combination of Baldur's context with state-tactic prediction.
- **Data Contamination Avoidance**: The use of a temporal split via automated GitHub extraction is highly novel and urgently needed for LLM evaluation in this domain.

### Novelty Verdict
Substantial

### Justification
While premise selection and state-tactic prediction are well-explored, the conceptual framing of evaluating LLM provers on *temporally held-out*, *long-context* real-world repositories is a significant and necessary shift. The community has overly fixated on miniF2F, which this paper correctly identifies as inadequate for testing context utilization. 

### Missing References
None identified. Key related works (LeanDojo, Baldur, miniF2F, PISA) are adequately cited.
