### Claims-to-Experiments Mapping
1. **Model evaluation:** Evaluated using the proposed $R_M^c$ metrics across 20 corruptions. Supported by Table 2, 3, 4.
2. **Subsampling validity:** Evaluated by comparing $0.05\%$ subsampling to full dataset. Supported by Table 5.
3. **Metric validity for object corruptions:** Evaluated by removing rain/snow pixels from metric calculation. Supported by Figure 6.
4. **Transferability to real-world:** Evaluated by testing models on the noisiest $10\%$ of KITTI frames. Supported by Figure 7.

### Baseline Assessment
The authors select a strong and representative set of models for optical flow (GMFlow, FlowFormer, RAFT, PWCNet, etc.), scene flow (M-FUSE, RAFT-3D), and stereo (ACVNet, LEAStereo, RAFT-Stereo). The baselines are not finetuned, which is appropriate for a generalization robustness benchmark. The variety covers different architectural paradigms (stacked, hierarchical, transformer).

### Dataset Assessment
The dataset is based on Spring, which is high-resolution and realistic. The corruptions are carefully implemented to be time-, stereo-, and depth-consistent. 
*Significant Concern:* As noted in Technical Soundness, the authors generate depth-dependent corruptions (like Fog) on the Spring test set using depths estimated by MS-RAFT+. This introduces data contamination, as the test set geometry will perfectly align with MS-RAFT+'s predictions.

### Metric Assessment
The metrics ($R_{EPE}^c$, $R_{1px}^c$, etc.) correctly quantify the robustness dimension (independent of accuracy). Using multiple complementary metrics is standard.

### Statistical Rigor
The results are derived from large-scale test sets (2000 frames per corruption $\times$ 20 corruptions). Variance reporting is inherently difficult for a large benchmark without running multiple seeds per model, but they report Average, Median, and Schulze rankings to provide a comprehensive view of performance across corruptions. 

### Ablation Assessment
They perform an excellent sanity check (Fig 6) showing that the corruption robustness score is stable even if the actual corruption pixels (e.g., rain) are excluded, meaning the metric captures the overall scene deterioration. They also successfully evaluate subsampling strategies.

### Missing Experiments
Ideally, the depth-consistent corruptions should have been validated on the Spring *validation* set where true ground truth depth is available, to avoid using estimated depths from a model that is subsequently benchmarked.

### Overall Experimental Rigor Verdict
**Mostly rigorous with gaps:** The benchmark design, baseline selection, and validation of the subsampling metric are excellent. However, using MS-RAFT+ to generate depths for the test set is a significant experimental design flaw for depth-dependent corruptions.