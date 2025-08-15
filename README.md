# SAKHA-AI
It's a local terminal ai which help u to run the file locally.
import os
from google import genai  # New SDK

# Configure client
client = genai.Client(api_key="YOUR_API_KEY")

# Create chat session with correct model
chat_session = client.chats.create(model='gemini-2.0-flash')

print("Welcome to AI Chatbot! Type 'exit' to end.")

while True:
    message = input("User> ").strip()
    if message.lower() == "exit":
        print("Chatbot session ended.")
        break
    
    try:
        response = chat_session.send_message(message=message)
        print("SAKHA> " + response.text)
    except Exception as e:
        print(f"Error: {e}")
