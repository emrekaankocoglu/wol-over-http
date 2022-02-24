import socketio

sio = socketio.Client()
macAndKey="none"
@sio.event
def connect():
    print('connection established')
    send_message(macAndKey)
@sio.event
def send_message(data):
    sio.emit('message',data)
    print('message ', data)
@sio.on('message')
def conf(data):
    print('message received with ', data)
@sio.event
def disconnect():
    print('disconnected from server')

def sendToServer(data):
    global macAndKey
    macAndKey=data
    sio.connect('http://0.0.0.0:5000')
    sio.disconnect()

