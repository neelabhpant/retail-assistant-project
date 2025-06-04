# streamlit_app.py
import streamlit as st
from config.config import settings
from crew.crew_setup import RetailCrew

def main():
    st.set_page_config(page_title="AI Retail Assistant", layout="wide")
    
    st.title("🛍️ AI Retail Assistant")
    st.markdown(f"**Model:** `{settings.openai_model_name}`")
    
    st.sidebar.header("About")
    st.sidebar.info(
        "This is an AI-powered retail assistant that uses a multi-agent system "
        "to answer your questions about products, orders, and company policies."
    )
    st.sidebar.header("Enter Customer ID")
    # You could use this input to automatically inject the customer ID into queries
    customer_id = st.sidebar.text_input("Customer ID", value="C001")


    # Main chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome! How can I help you today?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about products, your orders, or our policies..."):
        # Add user message to session state and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Create and run the crew with the new prompt
        with st.chat_message("assistant"):
            with st.spinner("Our AI team is on the case..."):
                # Append customer context to the prompt if needed
                full_prompt = f"I am customer {customer_id}. {prompt}"
                
                retail_crew = RetailCrew(full_prompt)
                result = retail_crew.run()
                
                st.markdown(result)
        
        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": result})

if __name__ == "__main__":
    main()