# This script loads the Chroma vector DB and defines the QA logic using LangChain.

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma

# Load existing Chroma vector DB
db = Chroma(
    persist_directory="vector_db",
    embedding_function=OpenAIEmbeddings()
)

# Define prompt template
prompt_template = """
You are a reliable medical assistant.
Answer the following question using only the information in the provided medical documents.

If the information is missing or unclear, reply with:
"I cannot answer based on the provided documents."

CONTEXT:
{context}

QUESTION:
{question}
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Create QA chain using retriever
retriever = db.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type_kwargs={"prompt": PROMPT})

def answer(question):
    return qa_chain.run(question)