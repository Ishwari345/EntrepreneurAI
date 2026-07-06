# --- Entrepreneur Bot (Offline) ---
# This program reads your 3 PDFs and answers questions from them

from gpt4all import GPT4All
from sentence_transformers import SentenceTransformer
# Import PersistentClient from chromadb for modern, persistent storage
from chromadb import PersistentClient 
# We no longer need to import Client or Settings for this simplified setup

from pypdf import PdfReader
import os # Import os for checking file existence

# 1️⃣ Load a small AI model (runs offline)
# Ensure your model path is correct. If the GPT4All model fails to load due to 
# DLL errors, you must install the Microsoft Visual C++ Redistributable.
model = GPT4All(r"C:\Users\ishwa\AppData\Local\nomic.ai\GPT4All\orca-mini-3b-gguf2-q4_0.gguf")

# 2️⃣ Create a small local memory for PDF info
# FIX: Use PersistentClient for modern, simple, persistent ChromaDB initialization
# The 'path' argument tells Chroma where to store the database files (in the './db' folder)
chroma_client = PersistentClient(path="./db")
collection_name = "entrepreneur_data"
collection = chroma_client.get_or_create_collection(collection_name)

# 3️⃣ Tool that understands text meaning
# NOTE: SentenceTransformer is often slow on first run as it downloads the model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 4️⃣ List your PDF file names (same as what you downloaded)
pdf_files = [
    "Entrepreneurship_Basics.pdf",
    "Startup_Process_and_Planning.pdf",
    "Entrepreneur_FAQ.pdf"
]

# Check if the collection is empty before processing and embedding the PDFs
# This prevents re-reading and re-embedding the files every time you run the script
if collection.count() == 0:
    print("📚 Reading your PDFs and building memory... please wait")
    
    # 5️⃣ Read and store info from the PDFs
    for pdf in pdf_files:
        if not os.path.exists(pdf):
            print(f"⚠️ Warning: File '{pdf}' not found. Skipping.")
            continue

        reader = PdfReader(pdf)
        text = ""
        for page in reader.pages:
            # Simple check to prevent errors on pages with no text
            if page.extract_text():
                text += page.extract_text()
        
        if text:
            # Simple chunking for demonstration (800 characters)
            chunks = [text[i:i+800] for i in range(0, len(text), 800)]
            
            # Generate embeddings and add to the collection
            embeddings = embedder.encode(chunks, show_progress_bar=False).tolist()
            
            # Create unique IDs for the chunks
            ids = [f"{pdf}_chunk_{i}" for i in range(len(chunks))]
            
            # Add to collection
            collection.add(
                documents=chunks, 
                embeddings=embeddings,
                ids=ids
            )

    print("✅ PDFs loaded! Memory is ready.")
else:
    print(f"✅ Memory already built with {collection.count()} chunks. Ready to ask questions.")

print("\n")

# 6️⃣ Chat loop
while True:
    question = input("Ask something about entrepreneurship (or type 'exit' to quit): ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    
    # Check if question is empty
    if not question.strip():
        continue

    try:
        # Find related info in PDFs
        q_embed = embedder.encode([question], show_progress_bar=False).tolist()
        
        # Query the vector store
        results = collection.query(
            query_embeddings=q_embed, 
            n_results=3,
            include=['documents'] # Only retrieve the text documents
        )
        
        # Combine the retrieved document chunks into a single context string
        context = "\n\n---\n\n".join(results["documents"][0])

        # Make the model answer using the context
        prompt = f"Using ONLY the information provided in the Context below, answer the Question. If the context does not contain the answer, state that you do not have enough information.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"
        
        print("\n🧠 Thinking... (may take a few seconds)")
        answer = model.generate(prompt)

        print("\n🤖 Bot:", answer.strip(), "\n")
        
    except Exception as e:
        print(f"\n❌ An error occurred during the chat process: {e}")
        print("Please check your LLM file path and ensure the model is running correctly.")
        break # Exit the loop on error