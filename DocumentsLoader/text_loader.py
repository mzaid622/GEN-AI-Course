from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = TextLoader("D:/GEN-AI-Course/DocumentsLoader/cricket.txt", encoding="utf-8")

docs = loader.load()
print(type(docs[0]))
