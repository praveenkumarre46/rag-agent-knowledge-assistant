from app.services.rag.embedder import Embedder
from app.services.rag.vector_store import VectorStore
from app.services.rag.document_loader import DocumentLoader


class RAGService:

    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()

        loader = DocumentLoader()
        docs = loader.load()
        chunks = loader.chunk(docs)

        embeddings = self.embedder.encode(chunks)
        self.vector_store.build_index(embeddings, chunks)

    async def handle_query(self, query: str) -> str:
        query_embedding = self.embedder.encode([query])

        docs = self.vector_store.search(query_embedding)

        answer = self.generate_answer(query, docs)
        return answer

    def generate_answer(self, query, docs):
        return f"Context: {docs} \nAnswer: Based on this, {query}"