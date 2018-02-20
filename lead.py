import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('submit')
def message(sid, data):
    # when a submit event is sent from client that means the user has solved a problem successfully
    # so all the users should update their leader board
    print("message ", data)
    # emit a changed event so clients can know that the leaderboard has been changed
    sio.emit('changed', {"data": "changed"})

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8081)), app)