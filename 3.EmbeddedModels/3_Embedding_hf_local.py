from langchain_huggingface import HuggingFaceEmbeddings

# Choose any embedding model
model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=model_name)

text = "This is a test sentence for embedding."
vector = embeddings.embed_query(text)

print("Embedding length:", len(vector))
print("First 10 values:", vector[:10])



