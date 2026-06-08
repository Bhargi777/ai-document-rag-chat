from app.services.rag_service import RagService

class HybridSearchService:
    def __init__(self):
        self.rag_service = RagService()

    def query(self, query_text: str, k: int = 5):
        # Placeholder for a hybrid retrieval approach combining keyword and semantic similarity.
        return self.rag_service.query(query_text)
