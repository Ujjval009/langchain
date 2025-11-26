from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv

load_dotenv()
model =ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, who won the world series in 2020?"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.contant))

print(messages)