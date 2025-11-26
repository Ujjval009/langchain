from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()  # loads HUGGINGFACEHUB_API_KEY

api_key = os.getenv("HUGGINGFACEHUB_API_KEY")
if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_KEY not found in environment variables.")

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=25,
    temperature=0.7,
    api_key=api_key  # <-- correct parameter name
)

response = llm.invoke("What is the capital of France?")
print("Response:", response)
