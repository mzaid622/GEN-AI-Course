from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0,
)

prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain Following Joke {text}", input_variables=["text"]
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)
print(chain.invoke({"topic": "black hole"}))
