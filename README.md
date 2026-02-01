🤖 Agentic AI RAG Chatbot
📌 Project Description

This project is an AI-powered Agentic RAG (Retrieval-Augmented Generation) Chatbot built using Python and LangGraph. The chatbot can understand user questions, retrieve relevant information from a knowledge base, and generate intelligent answers using a Large Language Model.

It also supports agentic behavior, meaning the AI can make decisions, follow multi-step workflows, and use tools or memory to improve responses. This project is beginner-friendly and designed for learning how modern AI agents and RAG systems work.

🚀 Features

Conversational AI chatbot powered by LLMs

Retrieval-Augmented Generation (RAG) for accurate answers

Built using LangGraph for agent workflows

Understands natural language questions

Retrieves relevant information using vector search

Can use tools and memory as part of agent reasoning

Beginner-friendly implementation in Jupyter Notebook or Python

🧰 Technologies Used

Python

LangGraph (for agentic workflows and orchestration)

OpenAI API (GPT models)

FAISS (vector database for similarity search)

NumPy, pandas

Jupyter Notebook / Python scripts

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/anushiyakandha/agentic-ai-chatbot.git
cd agentic-ai-chatbot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set your OpenAI API Key
export OPENAI_API_KEY="your_api_key_here"


(Windows PowerShell)

setx OPENAI_API_KEY "your_api_key_here"

4️⃣ Run the chatbot
python -m streamlit run app.py

💬 Sample Queries

Here are some example questions you can ask the chatbot:

"Summarize the main idea of the document."

"What are the key points discussed in this data?"

"Explain this topic in simple terms."

"Find information related to artificial intelligence."

"Give a short summary of the content."

"What tools can this AI agent use?"

🏗️ Architecture Overview

This project uses a Retrieval-Augmented Generation (RAG) architecture combined with a LangGraph-based AI agent workflow.

The user enters a question

The question is converted into vector embeddings

FAISS vector database retrieves the most relevant document chunks

Retrieved context is passed into the LangGraph agent workflow

The OpenAI LLM generates a response using the retrieved context

The agent can decide to use tools or memory before producing the final answer

The final answer is returned to the user

🔧 System Components

LangGraph → Manages multi-step reasoning and agent workflow

FAISS → Stores document embeddings for similarity search

OpenAI LLM → Generates intelligent natural language responses

Python Backend → Connects all components
