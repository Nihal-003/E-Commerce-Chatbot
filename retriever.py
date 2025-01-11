#importing necessary modules

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from sentence_transformers import SentenceTransformer


#retriever will search for most relevant answers based on user queries.
def setup_retriever(dataset: dict):
    
    
    #creating a list of document objects, where each document contains the answer as content and the question as metadata.
  
    documents = [
        Document(
            page_content=item["answer"], 
            metadata={"question": item["question"]}
        )
        for item in dataset["questions"]
    ]
    
    #initializing huggingFace model for embeddings
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = HuggingFaceEmbeddings(model=model)
    
    #creating a FAISS index from the document objects using the embeddings
    retriever = FAISS.from_documents(documents, embeddings)
    
    return retriever

