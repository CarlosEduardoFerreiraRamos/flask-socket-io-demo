from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'sshh'
socketio = SocketIO(app)

@app.route('/')
def home():
    return 'A Hello, from home'

@socketio.on('ws')
def ws(value):
    print('in socketio ws')
    emit('ws', 'through ws')

if __name__ == '__main__':
    socketio.run(app)