# This script loads medical documents, splits them into chunks, and stores them in a Chroma vector database.

import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load all .txt documents from the specified directory
directory = "data/guidelines"
documents = []

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        path = os.path.join(directory, filename)
        loader = TextLoader(path)
        docs = loader.load()
        documents.extend(docs)

# Split documents into manageable chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Create and persist Chroma vector database
db = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    persist_directory="vector_db"
)
db.persist()

print(f"\n✅ Chroma vector DB created with {len(chunks)} chunks from {len(os.listdir(directory))} files.")