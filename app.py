from flask import Flask, render_template, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    message = request.form['msg']
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        
    )
    bot_response = response.choices[0].message.content
    return jsonify(bot_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

