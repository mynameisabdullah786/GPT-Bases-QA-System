import nltk
nltk.download("punkt")

def split_text(text, chunk_size=200):

    sentences = nltk.sent_tokenize(text)

    chunks = []
    chunk = ""

    for sentence in sentences:

        if len(chunk) + len(sentence) < chunk_size:
            chunk += " " + sentence
        else:
            chunks.append(chunk)
            chunk = sentence

    chunks.append(chunk)

    return chunks