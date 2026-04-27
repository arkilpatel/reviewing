# Novelty Assessment

**1. Methodological and Conceptual Novelty:**
The paper introduces Rel-MOSS, a novel approach for addressing the class imbalance problem in Relational Deep Learning (RDL) applied to Relational Databases (RDBs). While class imbalance is a well-studied problem in traditional machine learning and homogeneous graph neural networks (e.g., GraphSMOTE), extending this to heterogeneous entity graphs derived from RDBs presents unique challenges. The authors propose two main contributions:
- **Rel-Gate (Relation-wise Gating Controller):** Modulates the message passing procedure for each relation to prevent minority class information from being submerged by majority class information. 
- **Rel-Syn (Relation-guided Minority Synthesizer):** An adaptation of SMOTE for heterogeneous graphs that integrates local relational structures (relational signatures) to maintain relational consistency when synthesizing new minority entities.

These contributions represent a substantial, though slightly incremental, conceptual advance. They logically combine attention/gating mechanisms with feature-space interpolation (SMOTE), adapted specifically for the structural constraints of heterogeneous RDB graphs.

**2. Empirical and Artifact Novelty:**
The paper is among the first to systematically investigate the class imbalance problem specifically within the context of the recently introduced RDL paradigm (e.g., RelBench). The problem formulation in this specific context is novel and practically motivated.

**3. Overall Novelty Rating:** Moderate to Substantial. The work successfully identifies a gap in the emerging RDL literature and provides a theoretically motivated, structurally aware solution. It is not entirely transformative, as it builds heavily on existing GNN gating and SMOTE paradigms, but the adaptation to RDBs is creative and highly relevant.

Score: 6