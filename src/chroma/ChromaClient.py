
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from typing import List

class ChromaClient():

    def __init__(self, chunk_size=500, chunk_overlap=0):

        # Text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        # Embeddings
        EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = SentenceTransformer(EMBEDDING_MODEL, trust_remote_code=True)

    def insert(self, doc):
        pass

    def delete(self, doc):
        pass

    def split_docs(self, docs):
        return self.text_splitter.split_documents(docs)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.model.encode(t).tolist() for t in texts]
    
    def embed_query(self, query: str) -> List[float]:
        return self.model.encode(query).tolist()