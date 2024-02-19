from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    content = request.json
    messages.append(content['message'])
    return jsonify({"status": "Message sent successfully"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(debug=True)
