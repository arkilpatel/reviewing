### Claimed Contributions
1. RSHBench, a benchmark for fine-grained diagnosis of factual and logical hallucinations in remote sensing VQA.
2. RADAR, a training-free inference method that leverages intrinsic attention in MLLMs to guide progressive localization (where) and fine-grained local reasoning (what) at test time.

### Prior Work Assessment
Visual cropping and adaptive zooming using attention maps from vision-language models have been explored in the MLLM literature prior to this work (e.g., ViCrop). However, tailoring a two-stage prompting and zooming inference process specifically for high-resolution, dense remote sensing imagery is a sensible and effective extension. The introduction of the RSHBench benchmark adds to the novelty.

### Novelty Verdict
Moderate

### Justification
The core technical idea—using attention maps for test-time cropping—is an incremental extension of existing visual grounding techniques. However, the specific two-stage (where-then-what) formulation and the new protocol-driven evaluation benchmark for RS-VQA elevate the contribution beyond a trivial application.

### Missing References
None glaringly missing; the paper correctly compares to region-based inference baselines like ViCrop.

Score: 5.0
