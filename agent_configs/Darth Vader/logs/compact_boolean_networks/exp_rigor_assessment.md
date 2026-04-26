### Experimental Rigor Assessment

1. **Benchmarks:** The evaluation is conducted on MNIST and CIFAR-10. While these datasets are considered trivial or solved in mainstream computer vision, they remain the standard benchmark for the emerging and computationally constrained field of end-to-end Boolean Logic Networks. 
2. **Baselines:** The authors compare against the exact state-of-the-art baselines relevant to their architecture (DiffLogicNet and TreeLogicNet) and use matching setups (thermometer encoding, population count decoder, data augmentation) to ensure fair comparisons.
3. **Ablation Studies:** The paper excels in its ablations. It isolating the effect of resampling versus simply increasing the number of candidate inputs, evaluates the impact of partial versus full layer connection learning, and explicitly compares progressive discretization against Gumbel noise injection.
4. **Performance:** The reported gains are massive and cleanly presented. Achieving better accuracy with 37x fewer Boolean operations (BOPs) on MNIST and 3x fewer on CIFAR-10 is a compelling empirical validation of the proposed techniques.

Score: 8.0