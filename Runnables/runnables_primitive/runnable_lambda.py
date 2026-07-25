from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from langchain_ollama import ChatOllama


def word_count(text):
    return len(text.split())


model = ChatOllama(
    model="tinyllama",
)

prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

chain2 = RunnableParallel(
    {"joke": RunnablePassthrough(), "count_word": RunnableLambda(word_count)}
)

final_chain = RunnableSequence(joke_gen_chain, chain2)

result = final_chain.invoke({"topic": "pakistan"})


final_result = """{} \n word count - {}""".format(result["joke"], result["count_word"])
print(final_result)
