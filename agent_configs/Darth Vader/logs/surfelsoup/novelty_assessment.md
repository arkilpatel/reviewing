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
