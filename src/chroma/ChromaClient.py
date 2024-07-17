
from chroma.ChromaEmbeddingClient import ChromaEmbeddingClient
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ChromaClient():

    def __init__(self, docs, chunk_size=500, chunk_overlap=0):

        # Text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        self.split_docs = self.text_splitter.split_documents(docs)

        # Embeddings
        EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = ChromaEmbeddingClient(EMBEDDING_MODEL)

    def insert(self, doc):
        pass

    def delete(self, doc):
        pass