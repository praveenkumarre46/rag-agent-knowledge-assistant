import ollama

class LLMService:

    def __init__(self):
        pass

    def generate(self, query, context):
        prompt = f"""
You are an intelligent AI assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Answer clearly and concisely:
"""

        response = ollama.chat(
            model='llama3',
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response['message']['content']