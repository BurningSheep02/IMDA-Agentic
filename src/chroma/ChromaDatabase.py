from chroma.ChromaClient import ChromaClient
from chroma.FileReader import FileReader
from langchain_chroma import Chroma
import os

class ChromaDatabase(ChromaClient):
    def __init__(self):
        super().__init__(self, 1000, 100)

        # Persistent vectorstore
        DB_DIR = f"{os.getcwd()}/chroma_db"
        if (os.path.exists(DB_DIR)):
            self.vectorstore : Chroma = Chroma(embedding_function=self.model, persist_directory=DB_DIR)
        else:
            docs = FileReader()
            self.vectorstore : Chroma = Chroma.from_documents(documents=docs, embedding=self.model, persist_directory=DB_DIR)

    def similarity_search(self, qn, k):
        res = self.vectorstore.similarity_search(query=qn, k=k)
        print("Similarity search finished on Chroma database\n")
        return res
    
    def insert(self, document):
        pass
        
