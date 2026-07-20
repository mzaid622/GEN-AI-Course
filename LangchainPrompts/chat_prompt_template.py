from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ##  [SystemMessage(content="You are a helpful assistant")] this is not work here
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)
