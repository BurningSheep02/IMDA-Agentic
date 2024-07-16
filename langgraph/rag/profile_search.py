from sentence_transformers import SentenceTransformer
from typing import List
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

import asyncio
from Summariser import Summariser

async def main():
    class MyEmbeddings:
        def __init__(self, model):
            self.model = SentenceTransformer(model, trust_remote_code=True)
    
        def embed_documents(self, texts: List[str]) -> List[List[float]]:
            return [self.model.encode(t).tolist() for t in texts]
        
        def embed_query(self, query: str) -> List[float]:
            return self.model.encode(query).tolist()


    loader = DirectoryLoader("/Users/shaoyang/Desktop/Agent/langgraph/rag/texts", glob="**/*.txt",show_progress=True)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    embeddings=MyEmbeddings("sentence-transformers/all-MiniLM-L6-v2")

    chromadb = Chroma.from_documents(
        documents=all_splits,
        embedding=embeddings,
    )

    question = ""
    docs = chromadb.similarity_search(question,k=3)
    relevant_texts = [document.page_content for document in docs]
    print(relevant_texts)

    legal_agent = Summariser()
    res = await legal_agent.summarise(relevant_texts,subject=question)
    return res

if __name__=="__main__":
    asyncio.run(main())