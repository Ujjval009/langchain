from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()  # loads your OPENAI_API_KEY

# Create the chat model (GPT-4.1 / GPT-4o-mini etc.)
model = ChatOpenAI(
    model="gpt-4o-mini",      # or "gpt-4.1", "gpt-4.1-mini", "gpt-4o"
    temperature=0.7
)

response = model.invoke("What is the capital of France?")
print("Response:", response.content)
