#Use it in Replit OpenAI Python GPT 3.5 Turbo Repl
#Kindly read the note README File.

from boltiotai import openai
import os
import sys

print("Welcome. I am a chatbot. I will do my best to answer your questions.")
print("Procced ahead and ask me anything.")
question=input("Q: Enter your question: \n")

while True:
    openai.api_key = os.environ['OPENAI_API_KEY']
    if openai.api_key == "":
        sys.stderr.write("""
        You haven't set up your API key yet.
    
        If you don't have an API key yet, visit:
    
        https://platform.openai.com/signup
    
        1. Make an account or sign in
        2. Click "View API Keys" from the top right menu.
        3. Click "Create new secret key"
    
        Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
        """)
        exit(1)
    
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
    "role": "system",
    "content": "You are a helpful assistant."
    },{
    "role": "user",
    "content": question
    }])

    output = response['choices'][0]['message']['content']
    print("Answer: ",output,"\n")

    choice=input("Do you want to continue ahead? (y/n): \n")
    if choice == "y":        
        question=input("Q: Enter your next question: \n ")
    else:
        print("Thank you for using me. Have a nice day.")
        exit(1)
