class DocumentLoader:

    def load(self):
        # For now, dummy knowledge
        return [
            "Artificial Intelligence is the simulation of human intelligence.",
            "Machine Learning is a subset of AI.",
            "Deep Learning uses neural networks."
        ]

    def chunk(self, docs):
        # simple chunking
        return docs