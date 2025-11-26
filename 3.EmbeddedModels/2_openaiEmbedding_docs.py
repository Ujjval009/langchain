from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
 
embeddings = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=36)

document =[
    "Delhi is the capital of India.",
    "Paris is the capital of France.",  
    "Tokyo is the capital of Japan."
]
result = embeddings.embed_documents(document)

print(str(result))