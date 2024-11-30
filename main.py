from flask import Flask, send_from_directory, request, jsonify
from flask_socketio import SocketIO, emit
import speech_recognition as sr
import time

app = Flask(__name__, static_folder='static', static_url_path='/')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    # Serve the Snake Game HTML
    return app.send_static_file('index.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    command = data.get('command')
    print(f"Received command: {command}")
    socketio.emit('command', {'command': command})
    return jsonify({"status": "success", "command": command})

@socketio.on('connect')
def on_connect():
    print("Client connected!")

@socketio.on('disconnect')
def on_disconnect():
    print("Client disconnected!")

def send_command_to_client(command):
    socketio.emit('command', command)

# Start the WebSocket server
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
