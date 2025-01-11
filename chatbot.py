from retriever import setup_retriever
from setup import GroqAI
from rag_chain import setup_rag_chain
from data_load import load_dataset, prepare_dataset
from dotenv import load_dotenv
import os

#loading environment variables from .env file
load_dotenv()

#path to your dataset
file_path = "C:/Users/Asus/Documents/chatbot/Ecommerce_FAQ _chatbot.json"

documents = load_dataset(file_path)
dataset = prepare_dataset(documents)

retriever = setup_retriever(dataset)

groq_ai = GroqAI()

rag_chain = setup_rag_chain(retriever, groq_ai)

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = rag_chain(user_query)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
