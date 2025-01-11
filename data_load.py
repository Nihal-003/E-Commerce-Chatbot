import json
from langchain.schema import Document

def load_dataset(file_path):
    #loading dataset in json format and returning list of documents.
    
    documents = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            question = item.get("Question", "").strip()
            answer = item.get("Answer", "").strip()
            if question and answer:
                documents.append(Document(page_content=answer, metadata={"question": question}))
    return documents

def prepare_dataset(documents):

    #converting the list to a dataset which is suitable for the retriever.
    return [{"question": doc.metadata["question"], "answer": doc.page_content} for doc in documents]
