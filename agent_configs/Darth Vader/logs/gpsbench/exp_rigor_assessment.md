### Claims-to-Experiments Mapping
1. **Model performance on GPS tasks**: Evaluated via zero-shot prompting on the 17 tasks of GPSBench across 14 models.
2. **Hierarchical degradation**: Evaluated specifically on the Place Association task across different administrative granularities (Country, Province, City).
3. **Robustness to noise / Memorization**: Evaluated by injecting Gaussian noise (10m to 1km) into coordinates and through a "Missing Data" probe.
4. **Downstream improvement**: Evaluated by appending coordinates to prompts for MapEval and Hierarchical Spatial benchmarks.
5. **Finetuning tradeoffs**: Evaluated by finetuning Qwen3-30B on the GPSBench training split and comparing to the zero-shot baseline.
6. **Model scale**: Evaluated by comparing performance across the Mistral and Qwen3 model families.

### Baseline Assessment
- **Appropriateness and Strength**: The baselines are very strong. The authors evaluate 14 state-of-the-art models, including the latest flagship models from OpenAI (GPT-5 series, GPT-4.1), Google (Gemini-2.5 series), Anthropic (Claude-4.5-Haiku), and open-weight leaders (Qwen3, Mistral). This provides a comprehensive and highly relevant snapshot of current frontier capabilities.
- **Completeness**: For the downstream tasks (MapEval, Hierarchical Spatial), comparing the base text prompt against the text prompt augmented with GPS coordinates is the perfect baseline to isolate the effect of coordinate injection. For finetuning, the zero-shot model serves as the appropriate baseline.

### Dataset Assessment
- **Relevance and Size**: The dataset is large (57,800 samples) and spans 17 well-defined tasks. 
- **Contamination**: By generating purely numeric and geodetic tasks directly from the GeoNames database using programmatic formulae, the authors significantly mitigate the risk of training data contamination. It is highly unlikely that the specific coordinate-pair distance computations exist verbatim in pretraining corpora.
- **Bias Mitigation**: The authors proactively use quota-based sampling to correct for the geographic skew in the GeoNames database (e.g., ensuring Africa is represented at 20% despite having fewer cities in the database). This is excellent experimental design.

### Metric Assessment
- **Mismatch**: As noted in the Technical Soundness evaluation, the aggregation of Accuracy and 1-MAPE into a single "Track Accuracy" score is problematic. While both are normalized to [0, 100], they measure fundamentally different things. A model that perfectly guesses 80% of multiple-choice questions but fails completely on 20% has an 80% accuracy. A model that answers every numerical question with a 20% error margin has an 80% 1-MAPE. Averaging these makes the aggregated numbers difficult to interpret rigorously. 

### Statistical Rigor
- **Variance**: The authors provide mean accuracy and standard deviation across the 14 LLMs (Figure 3), which is useful for understanding task difficulty.
- **Runs**: The finetuning experiment appears to be a single run on a single model. Given the stochasticity of LLM finetuning, reporting variance across multiple random seeds would strengthen the claim regarding capability trade-offs.

### Ablation Assessment
- The coordinate noise injection experiment acts as an excellent ablation on the precision of the input coordinates, successfully isolating whether the models rely on exact string memorization or generalized spatial representations.
- The downstream task augmentation isolates the specific impact of providing explicit coordinates to the LLM.

### Missing Experiments
- The finetuning experiment is limited to a single model (Qwen3-30B). While the result (trade-off between geometric computation and world knowledge) is intriguing, it is a strong claim to make based on a single model. Finetuning across different model sizes or architectures would be necessary to prove this is a universal phenomenon of LLMs rather than a quirk of Qwen3-30B's training recipe.

### Error Analysis Assessment
- The paper includes a solid error analysis, breaking down performance by geographic subregion. It highlights a stark 16.2% disparity in the Applied track between North America and East Asia, confirming that world-knowledge spatial reasoning inherits the geographic biases of pretraining data, while pure geometric computation does not. 

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

6.5