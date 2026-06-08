import os
from pathlib import Path
from typing import Protocol
from fastapi import UploadFile

class StorageProvider(Protocol):
    def save(self, file: UploadFile, destination: str) -> str:
        ...

class LocalStorageProvider:
    def __init__(self, base_path: str = ".storage"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save(self, file: UploadFile, destination: str) -> str:
        target = self.base_path / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("wb") as buffer:
            buffer.write(file.file.read())
        return str(target)

class S3StorageProvider:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def save(self, file: UploadFile, destination: str) -> str:
        # Placeholder for S3 storage upload implementation
        return f"s3://{self.bucket_name}/{destination}"
