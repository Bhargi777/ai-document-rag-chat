from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.config import get_settings
from app.services.prompt_templates import SYSTEM_PROMPT, CHAT_PROMPT
from app.services.rag_service import RagService

settings = get_settings()

class ChatChainService:
    def __init__(self):
        self.rag_service = RagService()
        self.llm = OpenAI(openai_api_key=settings.openai_api_key, model_name="gpt-4o")
        self.qa_chain = None

    def initialize_chain(self):
        if self.qa_chain is None:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.rag_service.vector_store.store.as_retriever(),
                return_source_documents=True,
            )

    def ask(self, query: str):
        self.initialize_chain()
        result = self.qa_chain.run(query)
        return result
