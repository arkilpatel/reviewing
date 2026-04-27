# Impact Assessment

This paper addresses logistic regression, which constitutes the final prediction layer of nearly all modern classification neural networks. The finding that hard labels inherently mislead rotation-invariant algorithms in identifying sparse targets is deeply impactful.

This result provides a theoretical justification for why techniques like label smoothing and knowledge distillation (which provide soft targets) might yield such significant empirical gains, particularly when the true underlying predictive features are sparse. Furthermore, it points toward simple architectural reparameterizations (like the $u \odot v$ spindly network) that can circumvent these fundamental limitations. This paper will likely influence both theoretical optimization literature and practical model design for classification tasks.

Score: 7.5
