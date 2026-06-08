from typing import List
from pathlib import Path

class PdfService:
    def extract_text(self, path: str) -> str:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found at {path}")
        # In production this should use a PDF parser like pypdf or pdfminer.
        return ""

    def extract_metadata(self, path: str) -> dict:
        return {"source": path, "pages": 0}

    def split_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        chunks: List[str] = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks
