from app.services.chat_chain import ChatChainService

class SummaryService:
    def __init__(self):
        self.chat_chain = ChatChainService()

    def summarize(self, content: str) -> str:
        prompt = f"Summarize the following document content in one paragraph:\n\n{content}"
        return self.chat_chain.ask(prompt)
