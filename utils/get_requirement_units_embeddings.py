from utils.get_embedding import get_embedding


def get_requirement_units_embeddings(requirement_units: list):
  requirement_units_with_embeddings = []

  for requirement_unit in requirement_units:
    embedding = get_embedding(requirement_unit['description'])
    requirement_unit['embedding'] = embedding
    requirement_units_with_embeddings.append(requirement_unit)

  return requirement_units_with_embeddings
