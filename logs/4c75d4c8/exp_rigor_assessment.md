### Experimental Rigor & Evaluation Assessment

**Claims-to-Experiments Mapping:**
- Claim: DexMachina outperforms baselines -> Supported by Section 5.1 (Figure 3 results on 4 hands and 7 tasks).
- Claim: Hybrid action space is superior -> Supported by Action Ablations (Section 5.2, Figure 8).
- Claim: VOC curriculum is better than physics-decay curriculum -> Supported by comparison with ManipTrans in Section 5.1/5.2.
- Claim: Hand embodiment comparisons -> Supported by Section 5.3 (Figure 5).

**Baseline Assessment:**
The baselines are strong and highly relevant. Comparing against recent concurrent/prior work (ObjDex [35] and ManipTrans [36]) is exactly what is expected. Crucially, the authors reimplemented these baselines in their own Genesis-based framework to ensure a fair comparison (same simulator advantages, same number of parallel environments, etc.). This is a highly rigorous practice that avoids the common pitfall of comparing a well-tuned new method in a fast simulator against an poorly-tuned old method in a slow simulator.

**Dataset Assessment:**
The use of ARCTIC demonstrations (5 articulated objects, diverse tasks like opening laptops, waffle irons, mixers) provides a challenging and appropriate testbed for long-horizon bimanual manipulation. 

**Metric Assessment:**
The paper proposes an ADD-AUC metric tailored for articulated objects. This is a robust choice that improves over simple binary success rates which are highly sensitive to arbitrary thresholds, capturing the continuous tracking quality of the policy throughout the trajectory.

**Statistical Rigor:**
The paper states that they run 5 random seeds for the main results and 3 random seeds for ablations. This meets the standard for RL evaluation. However, there is a slight gap in reporting: the text mentions "Averaged success rates... are reported", but it does not explicitly describe variance or standard deviations in the main text descriptions of the figures, though averaging multiple seeds is performed.

**Ablation Assessment:**
The ablation studies are well-designed. The action ablation effectively isolates the contribution of the hybrid action space vs. absolute or full residual actions. The comparison with the no-curriculum variant and the ManipTrans curriculum isolates the specific contribution of the Virtual Object Controllers.

**Overall Experimental Rigor Verdict:** Rigorous. The fair reimplementation of baselines is a major strength.