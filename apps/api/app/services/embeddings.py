from app.config import get_settings
from langchain.embeddings.openai import OpenAIEmbeddings

settings = get_settings()

class EmbeddingsService:
    def __init__(self):
        self.model = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

    def embed_texts(self, texts):
        return self.model.embed_documents(texts)

    def embed_query(self, query):
        return self.model.embed_query(query)
