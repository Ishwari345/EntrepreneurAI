# 🤖 EntrepreneurAI – Offline AI Entrepreneur Assistant using GPT4All

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that assists aspiring entrepreneurs by answering entrepreneurship-related questions using a local **GPT4All Large Language Model (LLM)** and a PDF-based knowledge base. The application runs entirely offline without requiring API keys, cloud services, or an internet connection after setup.

---

## 📌 Overview

**EntrepreneurAI** is an offline AI assistant developed to help students, entrepreneurs, and startup enthusiasts learn entrepreneurship concepts through natural language conversations.

Instead of relying on cloud-hosted AI services, the application uses a **local GPT4All model** and a **Retrieval-Augmented Generation (RAG)** pipeline. Entrepreneurship PDF documents are converted into vector embeddings and stored in **ChromaDB**, allowing the chatbot to retrieve relevant information and generate context-aware responses.

The project ensures complete privacy, offline accessibility, and zero dependency on external AI services.

---

## ✨ Features

- 🤖 Offline AI-powered chatbot
- 🧠 Local GPT4All Large Language Model
- 📚 Answers questions using entrepreneurship PDF documents
- 🔍 Semantic document retrieval with Sentence Transformers
- 💾 ChromaDB vector database for fast similarity search
- 📄 Supports multiple PDF knowledge sources
- 🚫 No API keys required
- 🌐 Fully offline after initial setup
- 💻 Interactive Streamlit web interface
- 🔒 Private and secure architecture

---

## 🏗️ System Architecture

```text
          Entrepreneurship PDFs
                   │
                   ▼
          Text Extraction (PyPDF)
                   │
                   ▼
   Sentence Transformer Embeddings
                   │
                   ▼
         ChromaDB Vector Database
                   │
      User Question (Semantic Search)
                   │
                   ▼
       Relevant Document Retrieval
                   │
                   ▼
          GPT4All Local LLM
                   │
                   ▼
      Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Large Language Model | GPT4All |
| Embeddings | Sentence Transformers |
| Vector Database | ChromaDB |
| Document Processing | PyPDF |
| Frontend | Streamlit |

---

## 📂 Project Structure

```text
EntrepreneurAI/
│
├── Knowledge_base/
│   ├── Entrepreneur_FAQ.pdf
│   ├── Entrepreneurship_Basics.pdf
│   ├── Entrepreneurship_Case_Studies.pdf
│   └── Startup_Process_and_Planning.pdf
│
├── db/                          # Generated ChromaDB vector database
├── app.py                       # Streamlit application
├── entrepreneur_bot.py          # Core chatbot logic
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### 1. Load Knowledge Base

The chatbot loads entrepreneurship PDF documents stored inside the **Knowledge_base** directory.

### 2. Extract Text

Text is extracted from each PDF using **PyPDF**.

### 3. Generate Embeddings

The extracted text is divided into smaller chunks and converted into vector embeddings using **Sentence Transformers**.

### 4. Store Vector Database

The generated embeddings are stored in **ChromaDB**, enabling efficient semantic retrieval.

### 5. Generate Responses

When the user asks a question:

- The query is converted into an embedding.
- ChromaDB retrieves the most relevant document chunks.
- The retrieved context is passed to GPT4All.
- GPT4All generates a context-aware response.

This workflow follows the **Retrieval-Augmented Generation (RAG)** architecture.

---

## 📖 Knowledge Base

The chatbot uses a curated entrepreneurship knowledge base consisting of:

- Entrepreneurship Basics
- Startup Process and Planning
- Entrepreneur FAQ
- Entrepreneurship Case Studies

Additional PDF documents can easily be added to the **Knowledge_base** folder to expand the chatbot's knowledge.

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Ishwari345/EntrepreneurAI.git

cd EntrepreneurAI
```

### Install Dependencies

```bash
pip install gpt4all chromadb sentence-transformers pypdf streamlit
```

### Download GPT4All Model

Download a compatible **GGUF** model from:

https://gpt4all.io/

Update the model path inside **entrepreneur_bot.py**.

---

## ▶️ Run the Application

### Terminal Version

```bash
python entrepreneur_bot.py
```

### Streamlit Interface

```bash
python -m streamlit run app.py
```

---

## 💬 Example Questions

- What is entrepreneurship?
- Who is an entrepreneur?
- Explain the startup process.
- What is a business plan?
- What are startup funding sources?
- Explain innovation in entrepreneurship.
- What is the difference between entrepreneur and intrapreneur?
- How can entrepreneurs manage risks?
- What are the common challenges faced by startups?
- Explain the importance of leadership in entrepreneurship.

---

## 🎯 Applications

- Entrepreneurship Learning Assistant
- Startup Guidance Platform
- Educational AI Chatbot
- Business Knowledge Assistant
- Offline AI Learning Tool
- Student Academic Project

---

## 🔒 Advantages

- Fully Offline Operation
- No API Keys Required
- No Cloud Dependency
- Fast Semantic Search
- Secure and Private
- Easily Extendable Knowledge Base
- Lightweight and User-Friendly

---

## 🔮 Future Enhancements

- Voice-based interaction
- Multi-language support
- User-uploaded PDF knowledge bases
- Conversation history
- Source citation for responses
- Improved UI/UX
- Support for larger local language models
- Docker deployment

---

## 👩‍💻 Author

**Ishwari Bagewadi**

Information Science Engineering Student

---

## 🙏 Acknowledgements

This project was built using the following open-source technologies:

- GPT4All
- Sentence Transformers
- ChromaDB
- Streamlit
- PyPDF
- Python Community

---
