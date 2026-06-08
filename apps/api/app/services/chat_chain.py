from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.config import get_settings
from app.services.prompt_templates import CHAT_PROMPT
from app.services.rag_service import RagService
from app.services.memory_service import MemoryService

settings = get_settings()

class ChatChainService:
    def __init__(self):
        self.rag_service = RagService()
        self.llm = OpenAI(openai_api_key=settings.openai_api_key, model_name="gpt-4o")
        self.memory = MemoryService()
        self.qa_chain = None

    def initialize_chain(self):
        if self.qa_chain is None:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.rag_service.vector_store.store.as_retriever(),
                return_source_documents=True,
                chain_type_kwargs={"prompt": CHAT_PROMPT},
            )

    def ask(self, query: str):
        self.initialize_chain()
        return self.qa_chain.run(query)
