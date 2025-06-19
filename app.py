import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '')
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=msg
    )
    return jsonify({'reply': response.text})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',8080)))
