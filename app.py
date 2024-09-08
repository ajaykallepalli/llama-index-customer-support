from flask import Flask, render_template, request, jsonify
from support_ai import SupportAI

app = Flask(__name__)
support_ai = SupportAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['query']
    response = support_ai.get_response(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)