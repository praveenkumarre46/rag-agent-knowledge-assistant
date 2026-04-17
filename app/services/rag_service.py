class RAGService:

    async def handle_query(self, query: str) -> str:
        docs = self.retrieve_docs(query)
        answer = self.generate_answer(query, docs)
        return answer

    def retrieve_docs(self, query):
        return ["This is dummy knowledge"]

    def generate_answer(self, query, docs):
        return f"Answer based on {docs}"