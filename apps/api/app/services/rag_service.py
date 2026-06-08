from app.config import get_settings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone, FAISS

settings = get_settings()

class RagService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
        self.vector_store = None

    def build_index(self, texts, ids):
        if settings.pinecone_api_key and settings.pinecone_environment:
            self.vector_store = Pinecone.from_texts(texts, self.embeddings, index_name=settings.pinecone_index)
        else:
            self.vector_store = FAISS.from_texts(texts, self.embeddings)

    def query(self, query_text: str):
        if self.vector_store is None:
            raise RuntimeError("Vector store not initialized")
        return self.vector_store.similarity_search(query_text)
