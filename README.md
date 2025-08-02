# Chat-PDFs

Absolutely! Here’s a polished and pretty version of your README with emojis, headings, and clean formatting:

---

# 📄💬 Chat with Your Documents

A simple web app that lets you **upload documents and chat with them** — like having a conversation with your PDFs!

---

## 🚀 Features

* 📂 **Upload Documents** — Easily add your own files to explore.
* 🧠 **Ask Questions** — Get intelligent answers from your document.
* 🧾 **OpenAI Embeddings** — Converts text into high-dimensional vectors to capture semantic meaning.
* 🗃️ **FAISS Vector Store** — Fast and efficient similarity search.
* 🔄 **LangChain Integration** —
  LangChain handles:

  * Persistent conversation memory
  * Chaining prompts and tools
  * Managing communication between your document and the language model.
* 🌐 **Streamlit Frontend** — Clean, interactive UI (deployment coming soon!).

---

## 🛠️ Tech Stack

| Tool                 | Purpose                                      |
| -------------------- | -------------------------------------------- |
| 🧠 OpenAI Embeddings | Turn text into numerical representations     |
| 🗃️ FAISS            | Store and search document chunks efficiently |
| 🔗 LangChain         | Chain LLMs with memory and document tools    |
| 🌐 Streamlit         | Frontend for user interaction                |

---

## 📝 To Do

* [x] Upload and process documents
* [x] Enable question-answering
* [x] Integrate LangChain for persistent chat
* [ ] Deploy using Streamlit Cloud

---

## 📎 How It Works (Simple Flow)

1. Upload a document
2. Text is split into chunks and embedded using OpenAI
3. Chunks are stored in a FAISS vector database
4. User asks a question
5. LangChain retrieves relevant chunks and sends them to the model
6. Answer is displayed in the chat UI

