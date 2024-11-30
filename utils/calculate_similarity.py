import numpy as np


def calculate_similarity(embedding1, embedding2):
  # Convert embeddings to numpy arrays if they are not already
  vec1 = np.array(embedding1)
  vec2 = np.array(embedding2)

  # Calculate the dot product and norms
  dot_product = np.dot(vec1, vec2)
  norm_vec1 = np.linalg.norm(vec1)
  norm_vec2 = np.linalg.norm(vec2)

  # Handle edge case for zero vectors
  if norm_vec1 == 0 or norm_vec2 == 0:
    return 0.0

  # Compute cosine similarity
  cosine_similarity = dot_product / (norm_vec1 * norm_vec2)

  # Ensure the result is between 0 and 1
  return max(0.0, min(1.0, cosine_similarity))
