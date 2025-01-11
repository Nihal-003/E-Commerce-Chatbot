def setup_rag_chain(retriever, groq_ai):
    
    #combining retriever and groq model to form the rag pipeline.
    
    def generate_answer(query):
        #retrieving relevant documents from the retriever
        results = retriever.similarity_search(query)
        
        #using groq ai to generate the response
        response = groq_ai.generate_response(query)
        
        return response

    return generate_answer

