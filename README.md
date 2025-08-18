
# SAKHA-AI Web Chatbot 💬🤖

**SAKHA-AI** is a lightweight **web-based chatbot** built with **Flask** and powered by Google’s **Gemini AI** models. It allows users to chat with an intelligent assistant directly from a browser, making it a simple yet powerful demonstration of integrating **Generative AI into web applications**.

## 📌 Overview
The application uses Flask to serve a minimalistic web interface where users can type in messages and receive real-time AI-generated responses. Conversations are displayed in a structured chat box format with clear distinction between user and bot messages.

The backend is powered by **Google Generative AI (Gemini)** through the `google-generativeai` Python package. A persistent chat session is maintained, allowing the AI to remember previous interactions within the same session, creating a more natural conversational experience.

## 🚀 Features
- Web interface for chatting with **Gemini AI**  
- Built with **Flask** (lightweight and easy to deploy)  
- Maintains **chat history** for contextual conversations  
- Clean and simple HTML/CSS interface  
- Easily extendable for more advanced AI-powered applications  

## ⚙️ How It Works
1. User types a message into the chat input box  
2. Flask receives the request and sends the input to Gemini AI  
3. Gemini generates a response, which is displayed back in the chatbox  
4. The conversation history is maintained during the session  

## 🔮 Future Improvements
- Adding authentication and user profiles  
- Enhancing UI/UX with modern front-end frameworks  
- Deploying on cloud platforms (Heroku, Render, or GCP)  
- Extending the chatbot to handle tasks like summarization, Q&A, or automation  

This project demonstrates how **Flask + Gemini AI** can be used to create an interactive AI assistant that runs locally and can be deployed anywhere.
