from flask import Flask, render_template_string, request
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA_vZmwsnJ7T2MGAorTh5handgtaEl0oss")  # replace with your real key
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

app = Flask(__name__)

# Simple HTML template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SAKHA Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .chat-box { width: 600px; margin: auto; border: 1px solid #ccc; padding: 20px; border-radius: 8px; }
        .user { color: blue; font-weight: bold; }
        .bot { color: green; font-weight: bold; }
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>🤖 Welcome to SAKHA Chatbot</h2>
        <form method="post">
            <input type="text" name="message" placeholder="Type your message..." style="width:70%" required>
            <button type="submit">Send</button>
        </form>
        <div>
            {% for m in history %}
                <p><span class="user">You:</span> {{m['user']}}</p>
                <p><span class="bot">SAKHA:</span> {{m['bot']}}</p>
                <hr>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_message = request.form["message"]
        response = chat.send_message(user_message)
        chat_history.append({"user": user_message, "bot": response.text})
    return render_template_string(TEMPLATE, history=chat_history)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
