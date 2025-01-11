from dotenv import load_dotenv
import os

#loading the .env file
load_dotenv()

class GroqAI:
    def __init__(self):
        #retrieving the API key from the .env file
        self.api_key = os.getenv("API_KEY")

    def generate_response(self, query: str):
        
        response = f"Generated response for: {query}"  
        return response
