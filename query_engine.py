import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

load_dotenv()

# Charger le prompt
with open("prompts/clinical_prompt.txt", "r") as f:
    template = f.read()

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)

# Charger la base vectorielle (avec désérialisation autorisée)
db = FAISS.load_local(
    "vector_db",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever()

# Créer la chaîne RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

def answer(question: str) -> str:
    return qa_chain.invoke({"query": question})