### Claims-to-Experiments Mapping
1. **Joint training works better than or equal to isolated training:** Supported by main results (Table 1 and extended tables in Appendix) comparing the unified SSA model to independently trained baselines.
2. **Generalization to unseen bands:** Supported by Section 4.4.2 (Houston and Loukia datasets).
3. **Generalization to unseen fractional scales:** Supported by Section 4.4.2 testing on 3.2x and 5.7x scales.

### Baseline Assessment
Baselines (DSPNet, MIMO-SST, DCINN, DCFormer, PSTUN, LRTN) are appropriate, recent, and cover transformer, CNN, and implicit network paradigms. However, there is a **Significant Gap** regarding the ablation of the joint training mechanism. The "w/o MK" baseline (Table 2) is trained independently on each dataset. To truly prove the value of the Matryoshka Kernel for joint training, the authors should have included a baseline where all datasets are zero-padded to $C_{max}$ and trained jointly using a standard fixed-channel convolution. Without this, it is unclear if the performance gain comes from the specific MK slicing mechanism or just from the increased data volume of joint training.

### Dataset Assessment
The use of 7 datasets (CAVE, Harvard, PaviaC, PaviaU, Chikusei, Botswana, WashingtonDC) is commendable and provides a highly rigorous, diverse testbed for multi-sensor fusion.

### Metric Assessment
PSNR, SAM, ERGAS, and SSIM are standard and comprehensive for evaluating HSI fusion. The inclusion of the SAM metric correctly tracks spectral fidelity.

### Statistical Rigor
The authors report standard deviations for their quantitative results, which indicates multiple runs or patch-level variance tracking. This is a strong positive. Model complexity and practical efficiency (FLOPs, runtime, peak memory) are thoroughly detailed in the appendix.

### Ablation Assessment
- **Component isolation:** The ablation of the MK component (Table 2) is flawed, as it confounds the removal of MK with the removal of joint training. 
- **Scale ablation:** Testing unseen fractional scales is robust and well-executed.

### Missing Experiments
1. **Zero-padding joint training baseline:** Train a standard network on all datasets jointly by zero-padding the spectral dimension to $C_{max}=191$ to isolate the true benefit of MK.
2. **True Zero-Shot Spectral Evaluation:** Section 4.4.2 uses 500 finetuning iterations. A strictly zero-shot evaluation on unseen bands is missing.

### Error Analysis Assessment
Error maps are provided visually in Figure 5, showing where models fail spatially. However, given the focus on spectral agnosticism, there is no error analysis of per-band spectral distortion, especially comparing the first 30 bands against the later bands, which is critical given the MK update imbalance.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

Score: 4.0 / 10