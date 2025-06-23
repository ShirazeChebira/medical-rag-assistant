# 🧠 Medical-RAG Assistant

This project is an **AI-powered medical assistant** that allows you to upload medical documents (PDF, DOCX, or TXT) and ask questions based on their content using a Retrieval Augmented Generation (RAG) architecture.

## 🚀 Features

* Upload medical PDFs, Word (DOCX) and text files
* Extracts and indexes content locally using Unstructured, Poppler and Tesseract
* Semantic search using OpenAI embeddings and Chroma vector database
* Ask natural language questions and receive answers strictly based on the uploaded documents
* Local processing — data privacy preserved

## 🛠️ Requirements

* Python 3.11+
* Poppler installed and added to PATH
* Tesseract installed and added to PATH
* OpenAI API key

## ⚙ Installation

1️⃣ Clone the repository:

```
git clone https://github.com/your-username/medical-rag-assistant.git
cd medical-rag-assistant
```

2️⃣ Create and activate virtual environment:

```
python -m venv venv
venv\Scripts\activate  # on Windows
```

3️⃣ Install dependencies:

```
pip install -r requirements.txt
```

## 🔑 API Key

Create a file `.env` at the root of the project:

```
OPENAI_API_KEY=your-openai-key-here
```

Or set it as environment variable before launching.

## 📂 Install Poppler

* Download Poppler for Windows:
  [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)
* Unzip and add `poppler-xx\Library\bin` to your PATH system variable.

## 📂 Install Tesseract OCR

* Download Tesseract OCR for Windows:
  [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* Install and ensure `C:\Program Files\Tesseract-OCR` is in your PATH.

## 🏃‍♂️ Run the app

```
streamlit run app.py
```

## ⚠ Limitations

* This app is for educational and research purposes only.
* It is not intended for clinical use or medical decision-making.

## 📄 License

Made by **Shiraze Chebira** - 2025 ❤️