Novelty:
The application of self-expressive properties (traditionally from Non-Rigid Structure from Motion) to streaming 3D reconstruction states to mitigate geometric drift is an interesting cross-pollination of ideas. Using a training-free sliding-window affinity matrix at inference time is a practical contribution over gradient-based test-time training (like TTT3R). However, the theoretical framing over-promises: claiming a "Grassmannian manifold perspective" when the actual algorithm reduces to a simple Euclidean moving-average using dot-product attention (Equation 9 and 10) dilutes the mathematical novelty. The core mechanism is essentially a temporal self-attention applied post-hoc.

Score: 5.5
