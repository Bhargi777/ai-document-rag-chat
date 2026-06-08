from langchain.prompts import PromptTemplate

SYSTEM_PROMPT = """
You are an AI assistant that answers questions using information from uploaded documents.
Provide concise answers and cite sources when available.
"""

CHAT_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
{system_prompt}

Context:
{context}

Question: {question}

Answer:""",
)
