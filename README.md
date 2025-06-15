# 🧬 Medical RAG Assistant

This project is a **medical assistant powered by Retrieval-Augmented Generation (RAG)** using OpenAI's GPT-3.5 and a vector database of medical documents.

It allows you to ask clinical or health-related questions, and it answers **only based on your own uploaded medical files**, with reliable and transparent behavior.

---

## 🚀 Features

- ✅ Medical Q&A with GPT-3.5 via RAG
- 📁 Custom document ingestion (vectorized with FAISS)
- 💬 Local chatbot interface using Streamlit
- 🌍 Supports multiple languages (English by default)
- 🔐 API key loaded securely via `.env`

---

## 📦 Technologies used

- [Python](https://www.python.org/)
- [OpenAI API](https://platform.openai.com/)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)

---

## ⚙️ How to run locally

```bash
# Clone this repository
git clone https://github.com/yourusername/medical-rag-assistant
cd medical-rag-assistant

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key in a .env file
echo OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx > .env

# Create the vector database
python retriever.py

# Run the chatbot UI
streamlit run app.py

## 📄 License

This project is for **educational and research purposes only**.  
It is **not intended for clinical use or patient decision-making**.

---

## 👩‍💻 Author

Made by **Shiraze Chebira**, 2025  
Powered by [OpenAI](https://openai.com/) & [LangChain](https://www.langchain.com/)
