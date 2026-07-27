from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("D:/GEN-AI-Course/DocumentsLoader/dl-curriculum.pdf")

documets=loader.load()
print(len(documets))
print(documets[0].page_content)
print(documets[0].metadata)
