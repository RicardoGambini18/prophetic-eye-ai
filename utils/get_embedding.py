from utils.openai_client import openai_client


def get_embedding(text):
  text = text.replace("\n", " ")
  return openai_client.embeddings.create(input=[text], model="text-embedding-3-large").data[0].embedding
