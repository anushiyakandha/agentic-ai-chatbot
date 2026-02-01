🤖 Agentic AI RAG Chatbot



📌 Project Description

The Agentic AI RAG Chatbot is an advanced intelligent assistant built using Python, LangGraph, and Large Language Models (LLMs). This project demonstrates how modern AI systems can combine reasoning, memory, and information retrieval to deliver accurate, context-aware, and human-like responses.

Unlike traditional chatbots that only generate responses based on prior training, this system uses Retrieval-Augmented Generation (RAG) to fetch relevant information from a knowledge base and combines it with LLM reasoning to produce more reliable and factual answers.

This chatbot is also agentic, meaning it can follow multi-step workflows, make decisions, and optionally use tools or memory during its reasoning process. The project is designed to help learners and developers understand the foundations of AI agents, RAG pipelines, and real-world AI system architecture.

This implementation serves as a practical introduction to next-generation AI assistants used in search engines, enterprise knowledge systems, research assistants, and automation platforms.

🚀 Features


💬 Intelligent conversational AI powered by LLMs

📚 Retrieval-Augmented Generation (RAG) for factual answers

🧠 Agentic workflow using LangGraph for multi-step reasoning

🔍 Semantic search using vector embeddings

🗂️ Context-aware responses based on retrieved documents

⚙️ Modular design for adding tools and memory

📈 Scalable architecture for future AI extensions

🧪 Beginner-friendly yet aligned with real-world AI systems

🧰 Technologies Used
Core Technologies


Python – Main programming language

LangGraph – Framework for building stateful, multi-step AI agent workflows

OpenAI API (GPT models) – Natural language understanding and response generation

Retrieval & Memory

FAISS – Vector database for similarity search

Embeddings Models – Convert text into numerical vectors

Data Processing

NumPy & Pandas – Data handling

Text processing libraries – Cleaning and preparing knowledge sources

Development Environment

Jupyter Notebook / Python Scripts – Interactive development and testing

⚙️ Setup Instructions


Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/anushiyakandha/agentic-ai-chatbot.git
cd agentic-ai-chatbot

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Your OpenAI API Key
export OPENAI_API_KEY="your_api_key_here"


(Windows PowerShell)

setx OPENAI_API_KEY "your_api_key_here"

5️⃣ Run the Chatbot
python -m streamlit run app.py


💬 Sample Queries


You can ask the chatbot questions such as:

"Summarize the main idea of the provided document."

"What are the key points discussed about artificial intelligence?"

"Explain this topic in simple terms."

"Find details related to machine learning in the knowledge base."

"Give a short and clear summary of the content."

"How does this AI agent decide what information to use?"

"What technologies are used in this project?"

🏗️ Architecture Overview



This system is built using a Retrieval-Augmented Generation (RAG) architecture combined with an Agentic AI workflow.

🔄 Workflow Steps

User Input – The user asks a question in natural language

Embedding Generation – The question is converted into a vector representation

Similarity Search – FAISS retrieves the most relevant document chunks

Context Injection – Retrieved information is passed into the LangGraph workflow

Agent Reasoning – The LangGraph agent decides how to process the information

LLM Response Generation – The OpenAI model generates a context-aware answer

Final Output – The chatbot returns an accurate and structured response

🧩 System Components


Component	Role
LangGraph	Controls agent reasoning flow and multi-step logic
FAISS	Stores document embeddings for fast retrieval
OpenAI LLM	Generates human-like responses
Python Backend	Connects retrieval, agent workflow, and response generation
🔮 Future Enhancements

🌐 Web interface using Streamlit 



🧠 Long-term memory for conversation history

🔧 Tool integration (web search, calculators, APIs)

📄 Support for multiple document types (PDF, CSV, websites)

🤝 Multi-agent collaboration workflows
