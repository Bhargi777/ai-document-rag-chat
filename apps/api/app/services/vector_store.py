from abc import ABC, abstractmethod
from app.services.embeddings import EmbeddingsService
from langchain.vectorstores import Pinecone, FAISS
from langchain.schema import Document
from app.config import get_settings

settings = get_settings()

class VectorStore(ABC):
    def __init__(self, embedder: EmbeddingsService):
        self.embedder = embedder

    @abstractmethod
    def add_documents(self, docs: list[Document]) -> None:
        ...

    @abstractmethod
    def similarity_search(self, query: str, k: int = 5):
        ...

class PineconeStore(VectorStore):
    def __init__(self, embedder: EmbeddingsService):
        super().__init__(embedder)
        self.client = None
        self.store = None

    def add_documents(self, docs: list[Document]) -> None:
        self.store = Pinecone.from_documents(docs, self.embedder.model, index_name=settings.pinecone_index)

    def similarity_search(self, query: str, k: int = 5):
        if self.store is None:
            raise RuntimeError("Pinecone store not initialized")
        return self.store.similarity_search(query, k=k)

class FaissStore(VectorStore):
    def __init__(self, embedder: EmbeddingsService):
        super().__init__(embedder)
        self.store = None

    def add_documents(self, docs: list[Document]) -> None:
        self.store = FAISS.from_documents(docs, self.embedder.model)

    def similarity_search(self, query: str, k: int = 5):
        if self.store is None:
            raise RuntimeError("FAISS store not initialized")
        return self.store.similarity_search(query, k=k)
