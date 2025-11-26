from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Load a local embedding model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedder = HuggingFaceEmbeddings(model_name=model_name)

# 2. Your documents
documents = [
    "Paris is the capital of France and known for the Eiffel Tower.",
    "The Python programming language is popular for AI and data science.",
    "Football is the most popular sport in the world.",
    "France is located in Europe and its capital city is Paris.",
]

# 3. Create embeddings for all documents
doc_vectors = np.array([embedder.embed_query(doc) for doc in documents])

# 4. Your query
query = "What is the capital of France?"

# 5. Create embedding for query
query_vector = np.array(embedder.embed_query(query))

# 6. Compute similarities
similarities = cosine_similarity([query_vector], doc_vectors)[0]

# 7. Get most similar document
most_similar_index = np.argmax(similarities)
most_similar_doc = documents[most_similar_index]

# 8. Display result
print("\nQuery:", query)
print("Most Similar Document:")
print(most_similar_doc)
print("Similarity Score:", similarities[most_similar_index])
