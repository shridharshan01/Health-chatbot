from flask import Flask, render_template, request, jsonify, session, send_file
import pandas as pd
from langchain_groq import ChatGroq
from io import BytesIO
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Load fine-tuning data
def load_fine_tuning_data(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

fine_tuning_data = load_fine_tuning_data('llm.csv')

# Model options
models = {
    "LLaMA3": ChatGroq(api_key="api key", model="llama3-8b-8192"),
    "Mixtral": ChatGroq(api_key="api key", model="mixtral-8x7b-32768")
}

@app.route('/')
def index():
    return render_template('index.html', model_names=models.keys())

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    selected_model = request.json.get('model', 'LLaMA3')
    model = models.get(selected_model, models["LLaMA3"])

    # Start session chat history
    if 'chat_log' not in session:
        session['chat_log'] = []

    # Check fine-tuning data
    for entry in fine_tuning_data:
        if user_input.lower() in entry['prompt'].lower():
            bot_reply = entry['response']
            break
    else:
        try:
            response = model.invoke(input=user_input)
            bot_reply = response.content.strip() if hasattr(response, 'content') else "Sorry, I didn't understand that."
        except Exception as e:
            bot_reply = f"Model error: {str(e)}"

    # Save to session chat log
    session['chat_log'].append({"user": user_input, "bot": bot_reply})
    session.modified = True

    return jsonify({'response': bot_reply})

@app.route('/download')
def download():
    chat_log = session.get('chat_log', [])
    if not chat_log:
        return "No chat history available."

    text_output = "\n".join([f"You: {msg['user']}\nBot: {msg['bot']}" for msg in chat_log])
    buffer = BytesIO()
    buffer.write(text_output.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='chat_log.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
