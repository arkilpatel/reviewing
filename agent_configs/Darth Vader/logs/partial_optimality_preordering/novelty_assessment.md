### Claimed Contributions
1. New partial optimality conditions for the NP-hard preordering problem.
2. Efficient algorithms to decide these conditions (cut, join, and fixation conditions).
3. Demonstration on real and synthetic datasets that these conditions efficiently fix a significant fraction of pairs in an optimal preorder.
4. Generalizing and proving prior conditions via improving maps (Shekhovtsov).

### Prior Work Assessment
- The preordering problem has been studied previously by Wakabayashi (1998) and more recently by Irmai et al. (2026).
- Partial optimality conditions were explored by Bocker et al. (2009) for clustering and orderings, and Stein et al. for related clustering problems.
- The use of improving maps for partial optimality traces back to Shekhovtsov (2013, 2014) and has been heavily applied to multicut and correlation clustering problems.
- The delta: This paper directly extends the improving maps framework from equivalence relations/symmetric preorders (clustering) and anti-symmetric preorders (partial ordering) to general preorders. This is a very predictable extension, taking known techniques from the correlation clustering / multicut literature and applying them to the joint relaxation (preordering). The novelty is highly incremental.

### Novelty Verdict
Incremental

### Justification
The paper essentially takes the improving maps machinery and existing partial optimality concepts (which the authors themselves note are "related to Thm. 1 of Lange et al. (2019)") and applies them to the directed preordering problem. While mathematically non-trivial, it is conceptually a straightforward and predictable step from existing work. The extension does not offer transformative new capabilities or deeply surprising insights into the structure of the problem beyond what would be expected from the correlation clustering analogues.

### Missing References
None apparent, they extensively cite the multicut and preordering literature.

Score: 3
