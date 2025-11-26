import streamlit as st
from transformers import pipeline

# -----------------------------
# Load a free Hugging Face model
# (TinyLlama or any small model)
# -----------------------------
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        tokenizer="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        max_new_tokens=100,
        temperature=0.7
    )

llm = load_model()

# -----------------------------
# Static Prompt
# -----------------------------
STATIC_PROMPT = """
You are a helpful assistant.
Write a short explanation in simple words about: 
{topic}
"""

# -----------------------------
# Streamlit App UI
# -----------------------------
st.title("🧠 Static Prompt Generator (Hugging Face + Streamlit)")

topic = st.text_input("Enter a topic:", "Machine Learning")

if st.button("Generate"):
    prompt = STATIC_PROMPT.format(topic=topic)

    with st.spinner("Generating..."):
        response = llm(prompt)[0]["generated_text"]

    st.write("### Output")
    st.write(response)
