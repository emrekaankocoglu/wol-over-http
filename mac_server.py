import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
def add_mac(data):
    f=open("index.php","r")
    content=f.readlines()
    ind=content.index('  <select name="select1">\n')
    label=data[22:]
    mac=data[4:21]
    f.close()
    if ind!=-1:
        content.insert(ind+1,'    <option value="'+mac+'">'+label+'('+mac+')'+'</option>\n')
        content="".join(content)
    f=open("index.php","w")
    f.write(content)
    f.close()
def remove_mac(data):
    f=open("index.php","r")
    content=f.readlines()
    label=data[22:]
    mac=data[4:21]
    ind=content.index('    <option value="'+mac+'">'+label+'('+mac+')'+'</option>\n')
    f.close()
    if ind!=-1:
        content.pop(ind)
        content="".join(content)
    f=open("index.php","w")
    f.write(content)
    f.close()

@sio.event
def send_message(data):
    sio.emit('message',data)
    print('message ', data)
@sio.on('message')
def multicast(sid,data):
    print("message",sid,data)
    if data.find("REQ ",0,4)==0:
        send_message(data[4:])
    elif data.find("ADD ",0,4)==0:
        add_mac(data)
    elif data.find("REM ",0,4)==0:
        remove_mac(data)
    else:
        print("Invalid message from client ",data,sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)