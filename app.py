from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


def background_thread():
    while True:
        socketio.emit('message', {'goodbye': "Goodbye"})
        time.sleep(5)


@socketio.on('connect')
def connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
