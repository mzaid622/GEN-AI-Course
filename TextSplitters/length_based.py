from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = "Paragraph 1: The Evolution of Artificial IntelligenceThe rapid evolution of artificial intelligence has fundamentally transformed how humanity interacts with technology and processes information. In its early stages, AI was limited to rule-based systems and basic automation, capable of executing only highly specific tasks within rigid, predefined parameters. However, the advent of modern machine learning and deep neural networks has unlocked unprecedented capabilities, enabling machines to learn from vast datasets, recognize complex patterns, and generate human-like responses. Today, large language models and autonomous agents are integrated into global industries, optimizing supply chains, accelerating scientific breakthroughs, and revolutionizing creative workflows. As these computational models grow increasingly sophisticated, the boundary between human intuition and machine calculation continues to blur, sparking critical global dialogues regarding data ethics, cognitive automation, and the long-term societal impacts of artificial intelligence."

loader = PyPDFLoader("D:/GEN-AI-Course/TextSplitters/dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")
result = splitter.split_documents(docs)

print(result[0])
    
