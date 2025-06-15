import streamlit as st
import os
from query_engine import answer
from retriever import create_vector_db

# 🩺 Configuration de la page
st.set_page_config(page_title="Medical RAG Assistant", page_icon="🩺", layout="centered")

# 💊 En-tête personnalisé
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color:#2c3e50;'>🩺 Medical Assistant (RAG-based)</h1>
        <p style='font-size: 1.1em; color:#4d4d4d;'>
            Ask clinical questions based <b>only</b> on your uploaded medical documents.<br>
            Uses <span style='color:#3498db;'>Retrieval-Augmented Generation (RAG)</span> with OpenAI & LangChain.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 📂 Upload des documents
st.subheader("📁 Upload your medical documents")
st.caption("Accepted formats: `.txt`, `.pdf`, `.docx`")

uploaded_files = st.file_uploader(
    label="Upload or drag medical files here",
    type=["txt", "pdf", "docx"],
    accept_multiple_files=True,
    label_visibility="collapsed"
)

if uploaded_files:
    os.makedirs("data/guidelines/", exist_ok=True)
    for file in uploaded_files:
        file_path = os.path.join("data/guidelines", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
    st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully.")

    with st.spinner("🔄 Updating medical database..."):
        create_vector_db()
    st.success("✅ Medical knowledge base updated.")

st.markdown("---")

# 💬 Zone de question
st.subheader("💬 Ask your question")
show_sources = st.checkbox("📄 Show source documents", value=False)

question = st.text_input("Your question:", placeholder="e.g. What is the treatment for hypertension?")

if question:
    with st.spinner("🔍 Searching medical documents..."):
        response = answer(question)

        if isinstance(response, dict):
            st.success(response.get("result", "No answer found."))
            if show_sources:
                st.markdown("### 🧾 Source documents")
                for doc in response.get("source_documents", []):
                    st.markdown(f"• *{doc.metadata.get('source', 'Unknown')}*")
        else:
            st.success(response)

# ✅ Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 0.9em; color: #555555;'>
        Made by <strong>Shiraze Chebira</strong>, 2025<br>
        Powered by <a href='https://openai.com' target='_blank'>OpenAI</a> & 
        <a href='https://www.langchain.com/' target='_blank'>LangChain</a> ⚡
    </div>
    """,
    unsafe_allow_html=True
)