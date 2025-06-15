import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

def load_documents(directory="data/guidelines/"):
    documents = []

    for filename in os.listdir(directory):
        if not filename.lower().endswith((".txt", ".pdf", ".docx")):
            continue

        path = os.path.join(directory, filename)
        ext = filename.lower().split(".")[-1]

        try:
            if ext == "txt":
                loader = TextLoader(path)
            elif ext == "pdf":
                loader = PyMuPDFLoader(path)
            elif ext == "docx":
                loader = Docx2txtLoader(path)
            else:
                continue
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")

    return documents

def create_vector_db():
    documents = load_documents("data/guidelines/")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    db = FAISS.from_documents(chunks, OpenAIEmbeddings())
    db.save_local("vector_db")
    print(f"✅ Vector DB created with {len(chunks)} chunks from {len(documents)} documents.")