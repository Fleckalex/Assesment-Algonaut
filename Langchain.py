


from langchain.document_loaders import TextLoader
loader=TextLoader('llama2_papers.txt')
from langchain.indexes import VectorstoreIndexCreator
index=VectorstoreIndexCreator().from_loaders([loader])

def build_llama_chatbot():
    # Main chatbot loop
    while True:
        user_input = input("User: ")

        # Exit the chatbot if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot exiting. Goodbye!")
            break

        

        # Extract the chatbot's response from the API response
        chatbot_response = index.query(user_input,llm=ChatOpenAI())
        # Print the chatbot's response
        print("Chatbot:", chatbot_response)