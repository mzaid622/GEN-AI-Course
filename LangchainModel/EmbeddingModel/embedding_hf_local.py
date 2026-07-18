from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]

vector = embedding.embed_documents(documents)

print(str(vector))

# import os
# from langchain_huggingface import HuggingFaceEmbeddings

# # Get your Ubuntu username dynamically
# username = os.getlogin()

# # Define the new folder on your Desktop
# desktop_model_path = f"/home/{username}/Desktop/huggingface_models"

# # Create the folder if it does not exist yet
# os.makedirs(desktop_model_path, exist_ok=True)

# # Set the environment variable using the os library
# os.environ["HF_HOME"] = desktop_model_path

# # Initialize the embedding (it will now download to your Desktop folder)
# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# documents = [
#     "Delhi is the capital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris is the capital of France",
# ]

# vector = embedding.embed_documents(documents)

# print(str(vector))
