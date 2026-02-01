from typing import TypedDict, List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langgraph.graph import StateGraph, END

# 1️⃣ Load & Process PDF
PDF_PATH = "D:\\DataScience\\agentic-rag-chatbot\\agentic_ai_ebook.pdf"

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)


# 2️⃣ LLM

llm = Ollama(model="tinyllama")


# 3️⃣ Graph State

class RAGState(TypedDict):
    question: str
    context: List[str]
    answer: str
    confidence: float


# 4️⃣ Retrieval Node (SMART FILTERING)

def retrieve_node(state: RAGState):
    results = vectorstore.similarity_search_with_score(state["question"], k=12)

    # FAISS returns LOWER score = BETTER match
    # We keep only strong matches
    filtered_docs = [(doc, score) for doc, score in results if score < 1.2]

    # If filtering removes too many, fallback to top 5
    if len(filtered_docs) < 3:
        filtered_docs = results[:5]

    context_chunks = [doc.page_content for doc, _ in filtered_docs]

    # Convert FAISS distance to confidence (0–1 scale)
    if filtered_docs:
        avg_distance = sum(score for _, score in filtered_docs) / len(filtered_docs)
        confidence = round(1 / (1 + avg_distance), 3)
    else:
        confidence = 0.0

    return {
        "context": context_chunks,
        "confidence": confidence
    }

# 5️⃣ Generation Node (STRICT GROUNDING)

def generate_node(state: RAGState):
    context_text = "\n\n".join(state["context"])

    prompt = f"""
You are a document-grounded AI assistant.

STRICT RULES:
1. Answer ONLY using the provided context
2. Do NOT use outside knowledge
3. If answer is missing, say: "Not found in the document."
4. Be clear and structured

Context:
{context_text}

Question: {state['question']}

Answer:
"""

    response = llm.invoke(prompt, timeout=60)

    return {"answer": response.strip()}

# 6️⃣ Build Graph
graph = StateGraph(RAGState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

rag_graph = graph.compile()
# 7️⃣ Main Function
def run_rag_pipeline(question: str):
    result = rag_graph.invoke({"question": question})

    return {
        "answer": result.get("answer", ""),
        "context": result.get("context", []),
        "confidence": result.get("confidence", 0.0)
    }
