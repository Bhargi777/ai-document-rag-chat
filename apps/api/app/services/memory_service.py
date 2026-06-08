from langchain.memory import ConversationBufferMemory

class MemoryService:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def get_memory(self):
        return self.memory

    def load_history(self, messages):
        for msg in messages:
            self.memory.chat_memory.add_user_message(msg.get("user", ""))
            self.memory.chat_memory.add_ai_message(msg.get("assistant", ""))
