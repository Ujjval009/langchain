from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
from langchain_core.prompts import PromptTemplate


# Load tiny LLM
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tokenizer="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=80,
    temperature=0.7,
)

llm = ChatHuggingFace(llm=HuggingFacePipeline(pipeline=pipe))

# STATIC PROMPT TEMPLATE
template = PromptTemplate(
    input_variables=[],
    template="Explain machine learning in very simple words."
)

prompt_text = template.format()   # no variables → static

response = llm.invoke(prompt_text)
print(response.content)

