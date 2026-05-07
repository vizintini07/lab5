from flask import Flask, jsonify
import time

app = Flask(__name__)

# Переменная для счетчика
request_count = 0

@app.route('/time', methods=['GET'])
def get_time():
    global request_count
    request_count += 1
    return jsonify({"time": int(time.time())})

# Новый роут для версии 2.0
@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({"count": request_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)