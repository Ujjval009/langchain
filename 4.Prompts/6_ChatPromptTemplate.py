from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

chat_template = ChatPromptTemplate([
    ('System', 'you are a helpful {domain} assistant.'),
    ('Human', 'Explain the concept of {topic} in simple terms')

]) 

prompt = chat_template.invoke({'domain': 'science', 'topic': 'photosynthesis'})

print(prompt)  # Displays the formatted messages with placeholders filled in



