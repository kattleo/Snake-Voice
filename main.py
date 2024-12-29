from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='/')

@app.route('/')
def index():
    # Serve the Snake Game HTML
    return app.send_static_file('index.html')

# Start the WebSocket server
if __name__ == "__main__":
    app.run(port=5000)
