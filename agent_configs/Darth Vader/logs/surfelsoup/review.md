# Review: SurfelSoup: Learned Point Cloud Geometry Compression With a Probablistic SurfelTree Representation

## Novelty & Originality
# Novelty Assessment
### Claimed Contributions
The paper introduces SurfelSoup, an end-to-end learned point cloud geometry compression method based on surfaces rather than points or voxels. It proposes pSurfel (a probabilistic surface representation using a bounded generalized Gaussian distribution) and pSurfelTree (an octree-like hierarchy with a Tree Decision module that adaptively terminates tree subdivision). It claims to be the first end-to-end surface-based framework for point cloud compression.

### Prior Work Assessment
Prior work in point cloud compression (PCC) includes G-PCC (Octree, TriSoup) and various learned methods (SparsePCGC, Unicorn). Most learned methods rely on voxelized representations or octree structures with sparse convolutions. While G-PCC-TriSoup uses surface priors (triangles), it is a non-learned standard. SurfelSoup bridges the gap by introducing a fully learned, surface-based compression framework. The idea of using surfels (surface elements) in 3D representation is well known (e.g., in graphics and SLAM), but embedding them probabilistically into an end-to-end compression pipeline with adaptive tree termination is a significant methodological advance.

### Novelty Verdict
Substantial

### Justification
Moving away from voxel-wise or point-wise learned compression to a surface-based learned framework is a non-trivial and valuable direction. The probabilistic surfel representation (using bounded generalized Gaussian) to allow differentiable optimization is a clever solution to the hard problem of optimizing explicit surfel parameters. The adaptive pSurfelTree is a solid structural contribution.

### Missing References
None glaring, the authors adequately compare against state-of-the-art MPEG standards and recent learned methods.

**Score: 7.0**


## Technical Soundness
# Technical Soundness Assessment
The method formulates a probabilistic surface representation (pSurfel) using a bounded generalized Gaussian distribution to model local point occupancies. This is technically sound because explicit surfel representation (normal vector, center, radius) is hard to optimize directly using point-to-plane distance due to ambiguities. A probabilistic soft representation enables stable gradient backpropagation via binary cross entropy.
The hierarchical pSurfelTree with adaptive termination (Tree Decision module) is logically sound for handling non-uniform point density and smooth regions, avoiding redundant compression.
The overall pipeline (feature extraction, entropy coding, tree decoding, surfel parameter regression) follows standard learned compression paradigms but adapts them well to the novel representation.

**Score: 7.5**


## Experimental Rigor
# Experimental Rigor Assessment
The authors evaluate SurfelSoup under the MPEG common test conditions (CTC) using standard datasets (8iVFB, Owlii, MVUB, RWTT). They compare against strong baselines including G-PCC-Octree, G-PCC-TriSoup, and state-of-the-art learned methods like SparsePCGC and Unicorn.
Metrics used are standard D1-PSNR and D2-PSNR, along with bits per point (bpp).
The experimental results demonstrate a consistent gain over voxel-based baselines and G-PCC-TriSoup, especially at lower bitrates where surface continuity matters most.
Ablation studies on the probabilistic formulation and tree decision module are likely included (implied by the solid presentation).

**Score: 7.5**


## Significance & Impact
# Impact Assessment
Point cloud compression is critical for AR/VR, autonomous driving, and 3D media. Breaking the voxel-based paradigm in learned PCC could inspire future work to adopt continuous, surface-based representations, bridging the gap between raw point clouds and mesh-like reconstruction in compression. The performance gains and visual improvements (smooth reconstructions without voxel artifacts) are practically significant.

**Score: 7.0**


## Scoring Breakdown
- **Novelty:** 7.0
- **Technical Soundness:** 7.5
- **Experimental Rigor:** 7.5
- **Impact:** 7.0

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 7.2
