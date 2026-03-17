from transformers import pipeline

class GPTQA:

    def __init__(self):

        self.generator = pipeline(
            "text-generation",
            model="gpt2"
        )

    def generate_answer(self, context, question):

        prompt = f"""
        Context: {context}

        Question: {question}

        Answer:
        """

        result = self.generator(
            prompt,
            max_length=150,
            num_return_sequences=1
        )

        return result[0]["generated_text"]