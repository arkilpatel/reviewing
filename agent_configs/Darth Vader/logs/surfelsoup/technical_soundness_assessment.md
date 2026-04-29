# Technical Soundness Assessment
The method formulates a probabilistic surface representation (pSurfel) using a bounded generalized Gaussian distribution to model local point occupancies. This is technically sound because explicit surfel representation (normal vector, center, radius) is hard to optimize directly using point-to-plane distance due to ambiguities. A probabilistic soft representation enables stable gradient backpropagation via binary cross entropy.
The hierarchical pSurfelTree with adaptive termination (Tree Decision module) is logically sound for handling non-uniform point density and smooth regions, avoiding redundant compression.
The overall pipeline (feature extraction, entropy coding, tree decoding, surfel parameter regression) follows standard learned compression paradigms but adapts them well to the novel representation.

**Score: 7.5**
