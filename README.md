# 🤖 Offline AI Entrepreneur Assistant using GPT4All

An intelligent **offline AI chatbot** that assists aspiring entrepreneurs by answering entrepreneurship-related questions using information extracted from PDF documents. The chatbot leverages a **local GPT4All Large Language Model (LLM)** combined with **Retrieval-Augmented Generation (RAG)** to provide context-aware responses without requiring any API keys or internet connection.

---

## 📌 Project Overview

The **Offline AI Entrepreneur Assistant** is designed to help students, aspiring entrepreneurs, and startup enthusiasts learn entrepreneurship concepts through an interactive chatbot.

Unlike cloud-based AI assistants, this chatbot runs entirely on the user's computer using a **local GPT4All model**. It retrieves relevant information from entrepreneurship PDF documents and generates accurate responses using a Retrieval-Augmented Generation (RAG) pipeline.

The project ensures complete privacy, offline accessibility, and zero dependency on external AI services.

---

## ✨ Features

- 🤖 Offline AI-powered chatbot
- 📚 Answers questions using entrepreneurship PDF documents
- 🧠 Local GPT4All Language Model
- 🔍 Semantic document search using Sentence Transformers
- 💾 Vector database powered by ChromaDB
- 🚫 No API Keys Required
- 🌐 No Internet Required after setup
- 📄 Supports multiple PDF knowledge sources
- 💻 Interactive Streamlit Web Interface
- 🔒 Private and Secure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| GPT4All | Local Large Language Model |
| Sentence Transformers | Text Embedding Generation |
| ChromaDB | Vector Database |
| PyPDF | PDF Text Extraction |
| Streamlit | Web Interface |

---

## 📂 Project Structure

```text
ENTREPRENEUR_BOT/
│
├── Knowledge_base/
│   ├── Entrepreneur_FAQ.pdf
│   ├── Entrepreneurship_Basics.pdf
│   ├── Entrepreneurship_Case_Studies.pdf
│   └── Startup_Process_and_Planning.pdf
│
├── db/                          # Vector database generated automatically
├── app.py                       # Streamlit Web Application
├── entrepreneur_bot.py          # Core chatbot logic
├── .gitignore                   # Git ignored files
└── README.md
```

---

## ⚙️ How It Works

### Step 1 – Load Knowledge Base
The chatbot reads entrepreneurship PDF documents from the **Knowledge_base** folder.

### Step 2 – Extract Text
Text is extracted from every PDF using **PyPDF**.

### Step 3 – Create Embeddings
The extracted content is divided into smaller chunks and converted into vector embeddings using **Sentence Transformers**.

### Step 4 – Store Embeddings
The embeddings are stored in **ChromaDB**, enabling fast semantic search.

### Step 5 – Answer User Queries

When a user asks a question:

- The question is converted into an embedding.
- ChromaDB retrieves the most relevant document chunks.
- GPT4All receives the retrieved context.
- The local language model generates an accurate response.

This workflow follows the **Retrieval-Augmented Generation (RAG)** architecture.

---

## 📖 Knowledge Base

The chatbot uses a curated entrepreneurship knowledge base consisting of multiple PDF documents, including:

- Entrepreneurship Basics
- Startup Process and Planning
- Entrepreneur FAQ
- Entrepreneurship Case Studies

The knowledge base can easily be expanded by adding more PDF files to the **Knowledge_base** folder.

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/EntrepreneurAI.git

cd EntrepreneurAI
```

---

### 2️⃣ Install Dependencies

```bash
pip install pypdf
pip install sentence-transformers
pip install chromadb
pip install gpt4all
pip install streamlit
```

---

### 3️⃣ Download GPT4All Model

Download any compatible GPT4All **GGUF** model from:

https://gpt4all.io/

Update the model path inside `entrepreneur_bot.py`.

---

## ▶️ Run the Project

### Terminal Version

```bash
python entrepreneur_bot.py
```

### Streamlit Interface

```bash
python -m streamlit run app.py
```

---

## 💬 Sample Questions

- What is entrepreneurship?
- Who is an entrepreneur?
- What are the characteristics of a successful entrepreneur?
- What are the different types of entrepreneurs?
- What are the steps involved in starting a business?
- Explain business planning.
- What is innovation?
- What are startup funding sources?
- What is the difference between entrepreneur and intrapreneur?
- How can entrepreneurs manage business risks?
- What are the common challenges faced by startups?
- Explain the role of leadership in entrepreneurship.

---

## 🎯 Applications

- Entrepreneurship Learning Assistant
- Startup Guidance System
- Educational AI Chatbot
- Business Knowledge Assistant
- Offline AI Learning Platform
- Student Academic Project

---

## 🔒 Advantages

- Fully Offline
- No API Keys Required
- No Cloud AI Dependency
- Fast Semantic Search
- Secure and Private
- Easy to Extend with More PDFs
- Lightweight and User-Friendly

---

## 🔮 Future Enhancements

- Voice-based Interaction
- Multi-language Support
- Upload Custom PDF Documents
- Conversation History
- Improved UI/UX
- Larger Local Language Models
- Cloud Deployment
- Mobile-Friendly Interface

---

## 👩‍💻 Author

**Ishwari Bagewadi**

---

## 🙏 Acknowledgements

This project was built using the following open-source technologies:

- GPT4All
- Sentence Transformers
- ChromaDB
- Streamlit
- PyPDF
- Python Community
