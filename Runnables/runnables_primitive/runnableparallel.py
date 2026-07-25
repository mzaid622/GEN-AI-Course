from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0,
)

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}", input_variables=["topic"]
)

llm = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, llm, parser),
        "linkedin": RunnableSequence(prompt2, llm, parser),
    }
)

result = parallel_chain.invoke({"topic": "black hole"})

print(result["tweet"])
print("----------------------------------------------------------------")
print(result["linkedin"])
