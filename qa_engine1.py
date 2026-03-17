from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np
import nltk

nltk.download("punkt")


class QAEngine:

    def __init__(self, document):

        # Load embedding model
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        # Load GPT generator
        self.generator = pipeline(
            "text-generation",
            model="gpt2"
        )

        # Split document into chunks
        self.chunks = self.split_text(document)

        # Create embeddings
        self.embeddings = self.embedder.encode(self.chunks)

        # Build FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(self.embeddings).astype("float32"))

    def split_text(self, text, chunk_size=200):

        sentences = nltk.sent_tokenize(text)

        chunks = []
        chunk = ""

        for sentence in sentences:

            if len(chunk) + len(sentence) < chunk_size:
                chunk += " " + sentence
            else:
                chunks.append(chunk.strip())
                chunk = sentence

        if chunk:
            chunks.append(chunk.strip())

        return chunks

    def search_context(self, question, top_k=3):

        query_embedding = self.embedder.encode([question])

        D, I = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        contexts = [self.chunks[i] for i in I[0]]

        return " ".join(contexts)

    def generate_answer(self, context, question):

        prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

        result = self.generator(
            prompt,
            max_length=150,
            num_return_sequences=1
        )

        return result[0]["generated_text"]

    def ask(self, question):

        context = self.search_context(question)

        answer = self.generate_answer(context, question)

        return answer