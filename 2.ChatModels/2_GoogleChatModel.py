from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads environment variables from .env

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # Use a supported model name
    temperature=0.7,
    google_api_key=api_key
)

response = llm.invoke("What is the capital of France?")
print("Response:", getattr(response, 'content', response))
