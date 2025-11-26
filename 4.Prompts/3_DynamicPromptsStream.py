import streamlit as st
from transformers import pipeline

# ------------------------------------------
# Load HuggingFace Model (cached in Streamlit)
# ------------------------------------------
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        tokenizer="google/flan-t5-small",
        max_new_tokens=120,
        temperature=0.7
    )

llm = load_model()

# ------------------------------------------
# Dynamic Prompt Template
# ------------------------------------------
DYNAMIC_PROMPT = """
You are a helpful assistant.
Follow the user's instructions and generate a clear answer.

Instruction: {instruction}
Context: {context}
"""

# ------------------------------------------
# Streamlit UI
# ------------------------------------------
st.title("⚡ Dynamic Prompt Generator (Hugging Face + Streamlit)")

instruction = st.text_input("Enter your instruction:", "Summarize this text")
context = st.text_area("Enter context text:", "Machine learning helps computers learn patterns from data.")

if st.button("Generate Output"):
    prompt = DYNAMIC_PROMPT.format(
        instruction=instruction,
        context=context
    )

    with st.spinner("Generating response..."):
        result = llm(prompt)[0]["generated_text"]

    st.write("### Output")
    st.write(result)
