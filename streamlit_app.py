# streamlit_app.py
import streamlit as st
from config.config import settings
from utils.llm_loader import llm

def main():
    st.set_page_config(page_title="AI Retail Assistant", layout="wide")

    st.title("🛍️ AI Retail Assistant")
    st.markdown(f"**Model:** `{settings.openai_model_name}` | **Embedding Model:** `{settings.embedding_model_name}`")

    # Test connection by printing a simple LLM completion
    with st.sidebar:
        st.header("Connection Test")
        if st.button("Test LLM Connection"):
            with st.spinner("Connecting to LLM..."):
                try:
                    response = llm.invoke("What is the color of the sky?")
                    st.success("Connection successful!")
                    st.write(response.content)
                except Exception as e:
                    st.error(f"Connection failed: {e}")

    # Main chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything about our products or your orders..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # This is a placeholder for now.
            # In Phase 4, this will call our agent crew.
            response = f"**Echo:** {prompt}"
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()