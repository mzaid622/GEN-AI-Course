from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite-001")

response = llm.invoke("Explain RAG in simple words")

print(response.content)
