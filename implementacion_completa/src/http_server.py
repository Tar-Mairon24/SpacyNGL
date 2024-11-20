from flask import Flask, request

app = Flask(__name__)

@app.route('/raw', methods=['POST'])
def raw_text():
    raw_data = request.data  # This retrieves the raw body of the request
    return f"Raw data received: {raw_data.decode('utf-8')}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
