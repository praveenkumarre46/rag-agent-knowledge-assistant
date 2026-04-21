import faiss
import numpy as np

class VectorStore:

    def __init__(self):
        self.index = None
        self.texts = []

    def build_index(self, embeddings, texts):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))
        self.texts = texts

    def search(self, query_embedding, k=2):
        distances, indices = self.index.search(query_embedding, k)
        return [self.texts[i] for i in indices[0]]