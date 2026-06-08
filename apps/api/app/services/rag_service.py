from app.services.embeddings import EmbeddingsService
from app.services.vector_store import PineconeStore, FaissStore
from app.config import get_settings
from langchain.schema import Document

settings = get_settings()

class RagService:
    def __init__(self):
        self.embeddings = EmbeddingsService()
        self.vector_store = self._select_store()

    def _select_store(self):
        if settings.pinecone_api_key and settings.pinecone_environment:
            return PineconeStore(self.embeddings)
        return FaissStore(self.embeddings)

    def build_index(self, docs: list[Document]) -> None:
        self.vector_store.add_documents(docs)

    def query(self, query_text: str):
        return self.vector_store.similarity_search(query_text)
