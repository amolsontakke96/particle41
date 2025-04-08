from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_info():
    user_ip = request.remote_addr
    timestamp = datetime.utcnow().isoformat() + "Z"

    return jsonify({
        "timestamp": timestamp,
        "ip": user_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
