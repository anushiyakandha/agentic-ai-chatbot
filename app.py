import streamlit as st
from rag_pipeline import run_rag_pipeline

st.set_page_config(page_title="Agentic AI RAG Chatbot", page_icon="🤖")

st.title("🤖 Agentic AI PDF Chatbot")
st.write("Ask questions based ONLY on the uploaded PDF document.")

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
question = st.chat_input("Ask a question from the PDF...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = run_rag_pipeline(question)

            answer = result["answer"]
            chunks = result["context"]
            score = result["confidence"]

            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"**Confidence Score:** {score}")

            with st.expander("📚 Retrieved Context"):
                for i, chunk in enumerate(chunks, 1):
                    st.write(f"**Chunk {i}:** {chunk[:500]}...")  # show first 500 chars

    st.session_state.messages.append({"role": "assistant", "content": answer})
