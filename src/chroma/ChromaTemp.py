from chroma.ChromaClient import ChromaClient
from langchain_chroma import Chroma
import os

class ChromaTemp(ChromaClient):
    def __init__(self, docs, query, k=5):
        super().__init__(self, 1000, 100)

        # Temporary vectorstore
        self.vectorstore : Chroma = Chroma.from_documents(documents=docs, embedding=self.model)
        res = self.vectorstore.similarity_search(query=query, k=k)
        print("Similarity search finished on temporary vectorstore\n")
        return res
        