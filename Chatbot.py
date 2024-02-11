import openai
import os
from openai import OpenAI
def read_llama2_papers_from_file(file_path='llama2_papers.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            llama2_papers = file.readlines()
        return llama2_papers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def build_llama_chatbot():
    llama2_papers = read_llama2_papers_from_file()

    if not llama2_papers:
        print("No llama2 papers available.")
        return

    # Concatenate llama2 papers into a single string for context
    documents = ' '.join(llama2_papers)

    # Main chatbot loop
    while True:
        user_input = input("User: ")

        # Exit the chatbot if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot exiting. Goodbye!")
            break

        # Create the prompt by combining user input and context
        prompt = f"User: {user_input}\nContext: {documents}\nChatbot:"
        messages=[]
        messages.append({"role": "user","content": user_input })
        # Make an API call to OpenAI GPT-3.5 Turbo


        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
            messages=messages,
            max_tokens=100,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.5,  # Adjust as needed
        )

        # Extract the chatbot's response from the API response
        chatbot_response = response['choices'][0].message.content
        messages.append({"role": "assistant","content": chatbot_response })
        # Print the chatbot's response
        print("Chatbot:", chatbot_response)

# Set your OpenAI API key
openai.api_key = os.getenv("openai_api_key") 


# Example usage
build_llama_chatbot()
