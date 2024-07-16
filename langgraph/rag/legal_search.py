from sentence_transformers import SentenceTransformer
from typing import List

class MyEmbeddings:
        def __init__(self, model):
            self.model = SentenceTransformer(model, trust_remote_code=True)
    
        def embed_documents(self, texts: List[str]) -> List[List[float]]:
            return [self.model.encode(t).tolist() for t in texts]
        
        def embed_query(self, query: str) -> List[float]:
            return self.model.encode(query).tolist()

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings

loader = DirectoryLoader("/Users/shaoyang/Desktop/Agent/langgraph/rag/penal code", glob="**/*.txt",show_progress=True)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

from langchain_chroma import Chroma
embeddings=MyEmbeddings("sentence-transformers/all-MiniLM-L6-v2")

chromadb = Chroma.from_documents(
    documents=all_splits,
    embedding=embeddings,
)


question = "mandatory death penalty for drug offences"
docs = chromadb.similarity_search(question,k=10)
relevant_texts = [document for document in docs]
print(relevant_texts)

from Summariser import Summariser
legal_agent = Summariser()
print(legal_agent.summariseSync(relevant_texts,subject=question))

