from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="tinyllama",  # Change if using another model
    temperature=0,
)

prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain Following Joke {text}", input_variables=["text"]
)


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)


chain2 = RunnableParallel(
    {"joke": RunnablePassthrough(), "explain": RunnableSequence(prompt2, model, parser)}
)

final_chain = joke_gen_chain | chain2

print(final_chain.invoke({"topic": "black hole"}))
