# 🧠 GenAI-Powered Document Q&A with Langchain + FAISS + Streamlit

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) system that lets users query their own documents using natural language. It uses **Langchain**, **FAISS** for vector storage, and a **Streamlit** interface for interaction with an **LLM** backend.

---

## 🚀 Use Case

A user uploads a PDF document and the system:
1. Reads and splits the content into chunks
2. Embeds the chunks and stores them in a **FAISS vector database**
3. Accepts user questions via **Streamlit UI**
4. Retrieves the most relevant chunks using similarity search
5. Uses a **Large Language Model (LLM)** (Mistral) to generate context-aware answers

---

## 🧱 Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| **Langchain** | Document loading, chaining, prompt templates |
| **FAISS**     | Local vector store for semantic search |
| **Streamlit** | Frontend UI for chat and document upload |
| **LLM (Mistral)** | For generating human-like responses |
| **Python**    | Glue for everything |

---

## 📁 Folder Structure
project-genai-rag-langchain/

├── main.py # Streamlit front end

├── backend/core.py #LLM code

├── Data/ # Test data

├── requirements.txt

├── README.md # You are here



---

## 🧪 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

2. **Run the Streamlit app from command prompt**
   ```bash
   streamlit run app.py
  ![image](https://github.com/user-attachments/assets/3f7a6bed-14ce-4dbe-a568-296b18965552)

3. **Start asking questions related to the document in Data folder**
   * "Give me a summary of this document, what it is about?"
     ![image](https://github.com/user-attachments/assets/4d27f3a2-a143-434e-8b0c-3573a71978d3)
   * ![image](https://github.com/user-attachments/assets/683e4363-8075-4567-bc72-00dfd1f53ad7)

📌 Highlights

✅ End-to-end GenAI pipeline

✅ Works with local/private documents

✅ Modular Python code

✅ Easy to extend (PDF loader, Azure hosting, etc.)

📫 Author

Sayon Bhattacharjee

Data Engineer | Pune, India

📧 sayon.bhattacharjee212@gmail.com

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)

