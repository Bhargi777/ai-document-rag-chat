from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Document RAG Chat API"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/ragchat"
    jwt_secret: str = "supersecret"
    jwt_algorithm: str = "HS256"
    openai_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_environment: str = ""
    pinecone_index: str = "rag-index"
    faiss_enabled: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
