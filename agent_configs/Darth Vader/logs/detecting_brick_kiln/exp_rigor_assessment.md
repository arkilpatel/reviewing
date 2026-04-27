# Experimental Rigor Assessment

### Claims-to-Experiments Mapping
1. **ClimateGraph Models Layouts Effectively:** Mapped to Table 2 (Graph-based models comparison).
2. **Systematic Comparison of Paradigms:** Mapped to the textual comparison in the Results Discussion, comparing Table 2 to Table 3. This mapping fails entirely because the evaluation setups (data, metric formulation) are incompatible.
3. **Zero-Shot Transfer of Foundation Models:** Mapped to Table 3, but the experiment for RemoteCLIP uses supervised linear probing (350 tiles/city), so the claim of zero-shot is unsupported by the experiment.

### Baseline Assessment
- The baselines for ClimateGraph (GAT, GCN, SAGEConv) are appropriate. However, they are evaluated on an unexplained formulation (graph nodes). 
- The foundation models are compared to the remote sensing baseline.
- The major gap is the lack of a unified baseline strategy. If ClimateGraph is the proposed method, it should be evaluated on the exact same image tiles and with the exact same metrics (e.g., bounding box IoU or tile-level binary classification) as the other methods to establish a true baseline comparison.

### Dataset Assessment
- The paper introduces a dataset of 1.3 million image tiles, yet states that "A total of 643 image tiles contain kiln instances". 
- The evaluation for foundation models inexplicably samples "500 tiles per city" (2,500 total). There is zero explanation of how these 500 tiles were sampled from the 1.3 million. Given the extreme class imbalance (643/1.3M), random sampling would yield almost no positive instances. If they balanced the subset, they must report how.
- The ClimateGraph model runs on "POIs". The method for identifying POIs from the 1.3 million tiles is omitted.

### Metric Assessment
- Table 2 reports Accuracy, Precision, Recall, and F1. Suspiciously, these four metrics have identical values for each model (e.g., 0.79 across the board for ClimateGraph, 0.62 for GCN). This usually indicates an error in metric computation.
- Table 3 reports "F1 Score", but the text for Rex-Omni describes its evaluation as "percentage of images with >= 1 valid bbox". 

### Statistical Rigor
- No standard deviations, error bars, or confidence intervals are reported. 
- The experiments appear to represent a single run, despite hardware and resource variation across the authors.
- There is no statistical significance testing.

### Ablation Assessment
- The ClimateGraph method introduces an anisotropic attention kernel, but there is no explicit ablation of this kernel versus isotropic attention within the same exact architecture. They merely compare it to completely different baselines (like standard GAT), which confounds architectural differences with the specific attention mechanism.

### Missing Experiments
- **A unified evaluation:** All methods must be evaluated on the exact same dataset split and the same metric.
- **POI generation pipeline:** If ClimateGraph is to be compared to image-based methods, there must be an end-to-end evaluation that includes the generation of the POI graph from the raw imagery.

### Error Analysis Assessment
- The paper lacks any deep qualitative error analysis. There are no images showing false positives, false negatives, or failure cases in heterogeneous urban environments, which is claimed to be a challenge. 

### Overall Experimental Rigor Verdict
Fundamentally flawed

**Experimental Rigor Score: 2.0 / 10**