from flask import Flask, request, jsonify, render_template
from qa_engine import QAEngine
import os

app = Flask(__name__)

qa_instances = {}


def load_document(doc_name):

    path = f"data/{doc_name}.txt"

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_qa_engine(doc):

    if doc not in qa_instances:

        text = load_document(doc)

        if text is None:
            return None

        qa_instances[doc] = QAEngine(text)

    return qa_instances[doc]


@app.route("/")
def home():
    return "QA System Running"


@app.route("/chat")
def chat():

    doc = request.args.get("doc", "documents")

    return render_template("chat.html", doc=doc)


@app.route("/ask", methods=["POST"])
def ask():

    question = request.json["question"]
    doc = request.json["doc"]

    qa = get_qa_engine(doc)

    if qa is None:
        return jsonify({"answer": "Document not found"})

    answer = qa.ask(question)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)