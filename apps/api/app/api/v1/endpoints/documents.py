from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from app.services.storage import LocalStorageProvider
from app.services.pdf_service import PdfService

router = APIRouter()

class UploadResponse(BaseModel):
    id: str
    title: str
    path: str

storage_provider = LocalStorageProvider()
pdf_service = PdfService()

@router.post("/upload", response_model=UploadResponse)
def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF uploads are supported")

    saved_path = storage_provider.save(file, f"uploads/{file.filename}")
    metadata = pdf_service.extract_metadata(saved_path)

    return {"id": file.filename, "title": file.filename, "path": saved_path}
