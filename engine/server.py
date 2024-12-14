from flask import Flask, jsonify, request
from waitress import serve
import subprocess

app = Flask(__name__)

def executeCommand(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

@app.route("/", methods=['GET'])
def root():
    return "Hi from server!"

@app.route("/archive", methods=['GET'])
def archive():
    data = request.get_json()  # Parse incoming JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400
    # Process the data (e.g., store it or return a response)
    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    executeCommand(["python3","./engine.py","softIoc:heartbeat","1"])
    serve(app, host='0.0.0.0', port=8000, threads=50)
