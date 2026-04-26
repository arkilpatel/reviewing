### Claims-to-Experiments Mapping
- **Claim 1 (Data efficiency):** Supported by Table 1 (Phone recognition on English benchmarks).
- **Claim 2 (Multilingual zero-shot):** Supported by Figure 4 and Table 8 (VoxAngeles benchmark).
- **Claim 3 (Dynamic switching helps under weak evidence):** Supported by Table 2 and Figure 6.
- **Claim 4 (Better acoustic-phonetic structure):** Supported by Figure 5 and Figure 7.

### Baseline Assessment
Baselines (Allosaurus, Allophant, W2V2-eSpeak, MultIPA, ZIPA, POWSM) are strong and appropriate state-of-the-art models for universal phone recognition. However, the fairness of the comparison is questionable due to the discrepancy in phonetic inventories (42 phones for HuPER vs. much larger narrow phonetic sets for baselines). The paper does not adequately detail how baselines with larger inventories are penalized or mapped in the PFER calculation. 

### Dataset Assessment
The datasets are appropriate and diverse (Buckeye, DRC-SE, L2-ARCTIC, EpaDB, SO762, VoxAngeles, and nfvPPA). Using human-annotated realized phones rather than G2P canonical transcripts is a massive strength of the experimental design, rigorously testing true phonetic perception.

### Metric Assessment
PFER (Phonetic Feature Error Rate) is the standard metric. However, PFER's sensitivity to the size of the underlying phone inventory is a known issue. Reporting a complementary metric, such as standard exact-match PER (Phone Error Rate), would provide a more complete picture. 

### Statistical Rigor
- **Variance reporting:** Missing. There are no standard deviations, confidence intervals, or multiple random seeds reported for the main results in Table 1.
- **Cherry-picking risk:** For Task-2 (Table 2), the authors report the results for "HuPER switched" using an optimal threshold $\tau^\star$ tuned on the test set. This is a methodological flaw. The threshold should be determined on a disjoint validation set; reporting the optimal $\tau^\star$ overestimates the performance of the dynamic scheduler.

### Ablation Assessment
There are significant gaps in the ablation studies. The paper attributes its data efficiency to the DRRC self-learning recipe, but it completely lacks an ablation of this component. There is no experiment comparing HuPER trained on the 100 hours *without* the DRRC Corrector, or with a naive pseudo-labeling baseline. This makes it impossible to verify if the gains come from DRRC or just the WavLM-Large backbone.

### Missing Experiments
1. **Ablation of DRRC components:** Performance of the initial TIMIT-only recognizer vs. naive pseudo-labeling vs. DRRC.
2. **Standard PER metric:** To rule out artifacts caused by the distinctive-feature distance mapping on the compact 42-phone inventory.
3. **Strict Validation-Test Split for $\tau$:** Evaluating the dynamic scheduler with a threshold chosen heuristically or on a validation set, rather than tuning on the test set.

### Error Analysis Assessment
The error analysis in Appendix E is excellent. It categorizes failures thoroughly (extreme evidence failures, wrong hypothesis conditioning, over-constrained top-down, scheduler outliers) and provides qualitative examples.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

5.5