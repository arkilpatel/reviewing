The experimental rigor is strong, particularly regarding the scaling laws and compute-efficiency analyses. The authors train over 100 models, carefully matching FLOP budgets across dnaHNet, StripedHyena2, and Transformer baselines. The inclusion of wall-clock benchmarks (throughput, peak memory, and latency) in the appendix alongside theoretical FLOP scaling provides a comprehensive and transparent view of the model's efficiency. 

The evaluation on zero-shot tasks (Protein Variant Effect Prediction via MaveDB and Gene Essentiality via DEG) convincingly demonstrates that dnaHNet outperforms StripedHyena2 at matched compute. The interpretability analysis (Table 1), which maps chunking boundaries to biological annotations in *B. subtilis*, is rigorous and provides compelling empirical evidence that the model is learning meaningful syntax rather than arbitrary compression.

The primary limitation in experimental rigor is the lack of fine-tuning evaluations and the restriction to prokaryotic genomes. While the authors transparently acknowledge these limitations, demonstrating performance on standard supervised genomic benchmarks or eukaryotic sequences would have elevated the empirical validation to the highest tier.

Experimental Rigor Score: 8.0
