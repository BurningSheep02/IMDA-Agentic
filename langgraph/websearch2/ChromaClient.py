import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings


class ChromaClient():

    def __init__(self):

        # Build the VectorStore from a list of given documents.

        self.CWD = os.path.dirname(os.path.realpath(__file__))

        self.loader = DirectoryLoader(f"{self.CWD}/files/", glob="**/*.txt")
        self.raw_docs = self.loader.load()

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        self.split_docs = self.text_splitter.split_documents(self.raw_docs)

        # Embeddings
        from sentence_transformers import SentenceTransformer
        from typing import List

        class MyEmbeddings:
            def __init__(self, model):
                self.model = SentenceTransformer(model, trust_remote_code=True)
        
            def embed_documents(self, texts: List[str]) -> List[List[float]]:
                return [self.model.encode(t).tolist() for t in texts]
            
            def embed_query(self, query: str) -> List[float]:
                return self.model.encode(query).tolist()
        
        from langchain_chroma import Chroma
        embeddings=MyEmbeddings("sentence-transformers/all-MiniLM-L6-v2")

        # Persistent vectorstore

        v_dir = f"{self.CWD}/chroma_db"
        if (os.path.exists(v_dir)):
            self.vectorstore : Chroma = Chroma(embedding_function=embeddings, persist_directory=v_dir)
        else:
            self.vectorstore : Chroma = Chroma.from_documents(documents=self.split_docs, embedding=embeddings, persist_directory=v_dir)

    def update_vectorstore(self):
        # Update the VectorStore with new documents in the folder.
        pass

    def similarity_search(self, qn, k):
        print("Similarity search finished")
        return self.vectorstore.similarity_search(query=qn, k=k)
