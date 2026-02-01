# ingestion.py
import os
from pathlib import Path
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# ---------------- Import Pinecone setup ----------------
from pinecone_setup import index  

# ---------------- PDF Reading ----------------
pdf_path = Path("C:\\Users\\ABINESH\\Downloads\\agentic-rag-chatbot\\agentic_ai_ebook.pdf")
pdf_reader = PyPDF2.PdfReader(str(pdf_path))
all_text = ""
for page in pdf_reader.pages:
    all_text += page.extract_text() + "\n"

# ---------------- Chunking ----------------
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(all_text)
print(f"Loaded {len(chunks)} chunks from the PDF")

# ---------------- Embeddings ----------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = embedding_model.encode(chunks)

# ---------------- Store in Pinecone ----------------
batch_size = 100 
for i in range(0, len(vectors), batch_size):
    batch = [(f"chunk-{j}", vectors[j].tolist(), {"text": chunks[j]})
             for j in range(i, min(i + batch_size, len(vectors)))]
    index.upsert(batch)

print(f"Stored {len(vectors)} chunks in Pinecone")
