from typing import List
from app.db.models import Document, DocumentChunk

class DocumentService:
    def create_document(self, owner_id: int, title: str, filename: str) -> Document:
        document = Document(owner_id=owner_id, title=title, filename=filename)
        return document

    def split_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks
