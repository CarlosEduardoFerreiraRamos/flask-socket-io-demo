from flask import Flask
from flask_socketio import SocketIO, emit
from tasks import app_task, app as celery
# from celery.result import AsyncResult

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'sshh'
socketio = SocketIO(app)

@app.route('/')
def home():
    print('on home')
    return 'A Hello, from home'

@app.route('/task/<t>')
def run_woeker(t):
    task = app_task.delay(int(t))
    return task.id

@app.route('/result/<id>')
def check_work(id):
    runnungTask = celery.AsyncResult(id)
    res = runnungTask.ready()
    print(res)
    if res:
        print(runnungTask.result)
        return runnungTask.result
    else:
        return 'In Process'

@socketio.on('ws')
def ws(value):
    print('in socketio edited in docker ws')
    emit('ws', 'through ws')

@socketio.on('connect')
def ws():
    print('in connect socketio ws')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0')