### Claimed Contributions
1. Formalizing the problem of model routing with a dynamic pool of LLMs, where new models appear at test time.
2. UniRoute: A routing approach that represents each LLM as a feature vector based on its prediction errors on a small validation set of representative prompts.
3. Two instantiations of UniRoute based on unsupervised (K-means) and supervised clustering.
4. Theoretical excess risk bound quantifying the error of the cluster-based routing.

### Prior Work Assessment
Because the paper is completely missing its bibliography (all citations are rendered as `[?]` and the reference list is empty), it is impossible to properly assess the gap against the specific prior work the authors intended to cite. However, based on the text, the closest prior work is K-NN routing and standard linear routing for static pools. 
The delta here is moving from a static assumption to a dynamic one by using empirical performance on a validation set as the LLM's feature representation, and then clustering prompts to generalize the error estimation.

### Novelty Verdict
Moderate.

### Justification
The idea of using validation set errors to represent an LLM's capabilities is a highly pragmatic and sensible approach to the dynamic routing problem. Extending K-NN to cluster-based average errors (both unsupervised and supervised) is a logical and moderately novel step that improves over raw K-NN by utilizing the larger unlabeled training distribution of prompts. However, the complete omission of the bibliography prevents a rigorous verification of whether concurrent work has already explored this exact dynamic routing setting. 

### Missing References
The entire bibliography is missing. Every single citation in the paper is a `[?]`.