import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader, UnstructuredWordDocumentLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Medical RAG Assistant", page_icon="🩺")

st.title("🩺 Medical RAG Assistant")
st.write("Upload a medical document (PDF, DOCX, or TXT) and ask questions based on its content.")

uploaded_file = st.file_uploader("Upload your medical document", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    file_path = os.path.join("temp_docs", uploaded_file.name)
    os.makedirs("temp_docs", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Choose loader based on file type
    if uploaded_file.name.endswith(".pdf"):
        loader = UnstructuredPDFLoader(file_path)
    elif uploaded_file.name.endswith(".docx"):
        loader = UnstructuredWordDocumentLoader(file_path)
    elif uploaded_file.name.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        st.error("Unsupported file type.")
        st.stop()

    st.info("Processing document...")
    docs = loader.load()

    # Split into chunks
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)

    # Create vector database
    db = Chroma.from_documents(chunks, OpenAIEmbeddings())

    # Prepare retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY),
        chain_type="stuff",
        retriever=db.as_retriever()
    )

    st.success("✅ Document processed. You can now ask your question.")

    question = st.text_input("Ask your medical question:")

    if question:
        answer = qa_chain.run(question)
        st.write("### Answer:")
        st.write(answer)