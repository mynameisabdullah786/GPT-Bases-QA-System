GPT-Based NLP Question Answering System (RAG + Chat Widget)

An advanced NLP Question Answering System that allows users to ask questions from documents using Retrieval Augmented Generation (RAG) and a beautiful embeddable chat widget (iframe).

🚀 Features

🔍 Ask questions from documents (TXT-based)

🤖 GPT-based answer generation

📚 Multi-document support (different iframe → different document)

⚡ Fast semantic search using vector embeddings

💬 Beautiful popup chat widget UI

🔌 Easy iframe integration into any website

🧠 Context-aware answers using RAG architecture

🧠 Tech Stack

Backend: Python + Flask

NLP Models: Hugging Face Transformers

Embeddings: SentenceTransformers

Vector Search: FAISS

ML Framework: PyTorch

Frontend: HTML, CSS, JavaScript (Chat UI)

📂 Project Structure
gpt_qa_system
│
├── app.py
├── qa_engine.py
│
├── data
│   ├── product_manual.txt
│   ├── insurance_policy.txt
│   └── legal_contract.txt
│
├── templates
│   └── chat.html
│
└── requirements.txt
⚙️ Installation
1. Clone Repository
git clone https://github.com/mynameisabdullah786/GPT-Bases-QA-System.git
cd gpt-qa-system
2. Install Dependencies
pip install -r requirements.txt

Or manually:

pip install flask transformers sentence-transformers faiss-cpu nltk torch
3. Download NLTK Data
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
▶️ Run the Application
python app.py

Open in browser:

http://127.0.0.1:5000/chat
💬 API Usage
Endpoint
POST /ask
Request
{
  "question": "Who created Python?",
  "doc": "product_manual"
}
Response
{
  "answer": "Guido van Rossum"
}
🧩 Embed Chat Widget (iframe)

You can embed the chatbot anywhere:

<iframe 
src="http://127.0.0.1:5000/chat?doc=product_manual"
width="380"
height="520"
style="border:none;">
</iframe>
📚 Multi-Document Support

Each widget loads a different document:

Widget	URL
Product Bot	/chat?doc=product_manual
Insurance Bot	/chat?doc=insurance_policy
Legal Bot	/chat?doc=legal_contract
⚡ How It Works (RAG Pipeline)

Document is split into chunks

Text is converted into embeddings

Stored in vector index using FAISS

User question → embedding

Top relevant chunks retrieved

GPT generates final answer

🖼️ UI Features

Floating popup chatbox

User & bot avatars

Chat bubbles

Smooth scrolling

Clean modern design

📈 Use Cases

Customer Support Chatbots

Legal Document Search

Insurance FAQ Assistants

Enterprise Knowledge Bots

Product Help Systems

🔥 Future Improvements

PDF / DOCX support

Streaming responses (like ChatGPT)

Voice input

Authentication system

SaaS multi-user dashboard

Deployment with Docker + AWS

🧑‍💻 Author

Md Abdullah Hannan

Transitioning into AI/ML & Data Science

13+ years in software development

Focus: NLP, Deep Learning, AI Systems
