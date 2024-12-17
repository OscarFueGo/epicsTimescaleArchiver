from flask import Flask, jsonify, request
from waitress import serve
import subprocess
import sys 
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Server started...")

app = Flask(__name__)

CORS(app)

processList = []
class ProcessManager:
    def __init__(self):
        self.processes = {}
    def activateArchiving(self, channel):
        process = subprocess.Popen(["python3","./engine.py",channel,"1"])
        self.processes[channel] =process
    def deactivateArchiving(self, channel):
        process = self.processes.get(channel)   
        if process:
            print(f"Stopping process for {channel} with PID {process.pid}")
            process.terminate()  # Graceful termination
            process.wait()
            del self.processes[channel]
            print(f"Process for {channel} stopped.")
        else:
            print(f"No process found for {channel}")

@app.route("/", methods=['GET'])
def root():
    logging.info("home...")
    return "Hi from server!"


@app.route("/stopArchive", methods=['GET'])
def stopArchive():
    channel = request.args.get('channel')
    manager.deactivateArchiving(channel)

@app.route("/archive", methods=['GET'])
def archive():
    channel = request.args.get('channel')
    manager.activateArchiving(channel)

if __name__ == '__main__':
    manager = ProcessManager()
    serve(app, host='0.0.0.0', port=8000, threads=50)
    sys.stdout.flush()