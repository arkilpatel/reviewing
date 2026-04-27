# Technical Soundness Assessment - "According to Me: Long-Term Personalized Referential Memory QA"

The paper's technical soundness is supported by its structured problem formulation and detailed evaluation framework.

### Strengths:
1. **Systematic Formulation:** The three-stage pipeline (Memory Ingestion, Retrieval, Answer Generation) provides a clear and modular framework for comparing different system designs.
2. **Schema-Guided Memory (SGM):** The implementation of SGM (incorporating OCR, entities, tags, and temporal/spatial metadata) is a technically sound way to normalize heterogeneous data for both retrieval and reasoning.
3. **Answer-Type–Aware Metric (QS):** The introduction of the Question Type Score (QS), which uses different metrics (EM, Jaccard, LLM-Judge) for different question types (Number, List, Open-ended), is a rigorous and sound approach to evaluating diverse personal QA outputs.
4. **Analysis of Baselines:** The implementation of 5 SOTA memory systems (A-Mem, Mem0, HippoRAG, etc.) is thorough and follows established protocols, making the performance comparisons credible.

### Weaknesses/Caveats:
1. **Reliance on LLM Judge:** While they validate GPT-5-mini against GLM-4.7, the use of LLM judges for open-ended questions still introduces some inherent subjectivity, though it's standard in current research.
2. **Simplicity of SGM:** While effective, the SGM schema is relatively static. A more dynamic or learned schema generation might be even more technically advanced, though SGM is a solid first step.
3. **Retrieval Bottleneck:** The finding that vision-language embeddings perform poorly (likely due to token dilution) is a critical technical observation, but the paper doesn't propose a complex solution beyond using text-based SGM.

### Assessment:
The paper is technically very sound. The evaluation framework is robust, and the experimental comparisons between DM and SGM, and between Piled and Linked memory, provide clear technical insights into what works (and what doesn't) in this new domain.

**Score Recommendation (Technical Soundness): 9.0/10** (Rigorous evaluation framework and sound methodology).