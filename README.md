This project is an AI-powered retail assistant designed to intelligently respond to customer queries in natural language. It leverages a multi-agent system built with CrewAI, Retrieval-Augmented Generation (RAG) for accessing knowledge bases, and specialized tools for performing specific retail-related tasks. The primary goal is to provide a seamless and efficient customer experience by understanding complex queries and providing comprehensive answers.
# 🛍️ AI Retail Assistant Project

## Features

* **Multi-Agent System:** Utilizes CrewAI to orchestrate a team of specialized AI agents (Query Router, Retail Assistant, Summarizer).
* **Natural Language Understanding:** Processes complex, multi-intent user queries.
* **Retrieval-Augmented Generation (RAG):**
    * Answers frequently asked questions (FAQs) by searching an embedded knowledge base.
    * Searches a product catalog semantically to find relevant items.
* **Specialized Tools:**
    * **Order History Tool:** Retrieves customer order details.
    * **Return Item Tool:** Processes return requests based on defined business logic.
    * **FAQ Tool:** Provides answers from a pre-defined set of frequently asked questions.
    * **Product Search Tool:** Finds products based on user descriptions.
* **Conversational UI:** Built with Streamlit for an interactive chat experience.
* **Persistent Knowledge:** Uses ChromaDB (via Docker) as a vector store for RAG data.


## High-Level Architecture

1.  **User Interface (Streamlit):** Captures user queries.
2.  **CrewAI Pipeline:**
    * **Query Router Agent:** Analyzes the query and identifies distinct intents.
    * **Retail Assistant Agent:** Executes specific tasks based on routed intents using specialized tools (Order History, Return Item, FAQ Search, Product Search).
    * **Summarizer Agent:** Consolidates information from the Retail Assistant Agent and crafts a single, coherent response.
3.  **Tools & Data Layer:**
    * Tools interact with structured data (JSON for orders, CSV for products) and unstructured data (text files for FAQs).
    * RAG tools query ChromaDB, which stores embeddings of FAQs and product information.
  
![Screenshot 2025-06-10 at 12 13 25 PM](https://github.com/user-attachments/assets/93b54b48-4b3c-4066-b435-645626ff4a14)


## Setup and Installation

### Prerequisites

* Python 3.10+ (Python 3.12 recommended)
* Pip (Python package installer)
* Docker Desktop (for running ChromaDB)
* An OpenAI API Key

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/neelabhpant/retail-assistant-project.git](https://github.com/neelabhpant/retail-assistant-project.git)
    cd retail-assistant-project
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    * Create a `.env` file in the root directory of the project.
    * Add your OpenAI API key to the `.env` file

5.  **Start ChromaDB using Docker:**
    * Run the following command in your terminal to start the ChromaDB container:
        ```bash
        docker run -d -p 8000:8000 --name chroma-db chromadb/chroma
        ```
    * To make the ChromaDB data persistent across container restarts, use a Docker volume:
        ```bash
        docker run -d -p 8000:8000 -v chroma_data_retail:/chroma/chroma --name chroma-db-persistent chromadb/chroma
        ```

6.  **Embed Data into ChromaDB:**
    * Run the embedding scripts from the project root directory. These scripts will populate ChromaDB with your FAQ and product data.
        ```bash
        python -m rag.embed_faqs
        python -m rag.embed_products
        ```

## ▶How to Run

Once the setup is complete, you can run the Streamlit web application:

1.  Ensure your virtual environment is activated and the ChromaDB Docker container is running.
2.  From the root directory of the project, run:
    ```bash
    streamlit run streamlit_app.py
    ```

## Future Enhancements (Potential)

* **Streaming Responses:** Stream agent responses token-by-token in the UI.
* **Display Agent Thoughts:** Provide users with insights into the agent's decision-making process.
* **Action-Oriented Tools:** Develop tools that can modify data or trigger external actions (e.g., actually processing a return, sending an email).
* **Live Database Integration:** Connect tools to real-time databases instead of static files.
* **Evaluation Suite:** Create a comprehensive set of tests to measure accuracy and performance.
* **Deployment:** Package the backend as a FastAPI and deploy frontend/backend separately.
