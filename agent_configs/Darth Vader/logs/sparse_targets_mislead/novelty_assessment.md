# Novelty Assessment

This paper identifies a fundamental gap in the learning dynamics of rotation-invariant algorithms (such as standard fully-connected networks trained with Gradient Descent) versus non-rotation-invariant algorithms (such as spindly-parameterized networks where $w_i = u_i v_i$) in the setting of over-constrained sparse logistic regression. 

While the failure of rotation-invariant algorithms under under-constrained or noisy settings is known, the authors isolate a subtle and highly novel observation: even in the over-constrained regime ($n > d$) and without any additive label noise, merely observing sampled hard labels from a sparse target (rather than true soft conditional probabilities) is sufficient to introduce enough randomness to handicap rotation-invariant algorithms.

Developing the lower bounds for logistic loss over a spherical posterior and the upper bounds via state-dependent Riccati-type ODEs are non-trivial theoretical advances over prior square-loss analyses. This is a very creative and novel theoretical result.

Score: 8.0
