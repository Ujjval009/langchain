from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_KEY")

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=150,
    temperature=0.7,
    api_key=api_key
)

chat_history = []

print("Chatbot started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Build prompt with history for chat models
    prompt = ""
    for turn in chat_history:
        prompt += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    prompt += f"User: {user_input}\nAssistant:"

    response = llm.invoke(prompt)
    bot_reply = response.strip()
    print("Bot:", bot_reply)

    chat_history.append({
        "user": user_input,
        "bot": bot_reply
    })