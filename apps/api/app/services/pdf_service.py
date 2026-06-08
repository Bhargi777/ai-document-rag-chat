from typing import List
from pathlib import Path
from pypdf import PdfReader

class PdfService:
    def extract_text(self, path: str) -> str:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found at {path}")

        reader = PdfReader(str(file_path))
        text_lines: List[str] = []
        for page in reader.pages:
            text_lines.append(page.extract_text() or "")
        return "\n\n".join(text_lines)

    def extract_metadata(self, path: str) -> dict:
        file_path = Path(path)
        reader = PdfReader(str(file_path))
        return {
            "source": str(file_path.name),
            "pages": len(reader.pages),
        }

    def split_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        chunks: List[str] = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks
