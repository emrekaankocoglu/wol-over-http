import socketio
import hashlib
import subprocess
import sys
sio = socketio.Client()
hash_key_pairs={"hash":"label(mac)"}
def restore_dict():
    global hash_key_pairs
    f=open("pairs.txt","r")
    for line in f:
        key, value = line.split()
        hash_key_pairs[key] = value
def dict_to_file():
    with open('pairs.txt', 'w') as f:
        for key in hash_key_pairs.keys():
            f.write("%s %s\n" %(key, hash_key_pairs[key]))
    f.close()
@sio.event
def connect():
    print('connection established')
@sio.on('message')
def conf(data):
    print('message received with ', data)
    pair_check(data)
@sio.event
def disconnect():
    print('disconnected from server')
@sio.event
def send_message(data):
    sio.emit('message',data)
    print('message ', data)
def pair_check(hash_key):
    pair_present=hash_key_pairs.get(hash_key,False)
    if pair_present==False:
        print("Key not found")
    else:
        subprocess.run(['wakeonlan',pair_present[-18:-1]])
        print("Packet sent to "+pair_present)
def add_pair(mac_addr,key,label):
    macKeyPairSHA3_256Str=string_hash(mac_addr,key)
    hash_key_pairs[macKeyPairSHA3_256Str]=label+"("+mac_addr+")"
    send_message("ADD "+mac_addr+" "+label)
    dict_to_file()
    return "Pair added"
def remove_pair(mac_addr,key,label):
    str=string_hash(mac_addr,key)
    success=hash_key_pairs.pop(str,-1)
    if success!=-1:
        send_message("REM "+mac_addr+" "+label)
        dict_to_file()
def string_hash(mac_addr,key):
    macKeyPair=mac_addr+"-"+key
    macKeyPairEnc=macKeyPair.encode()
    macKeyPairSHA3_256=hashlib.sha3_256(macKeyPairEnc)
    macKeyPairSHA3_256Str=hashlib.sha3_256(macKeyPairEnc).hexdigest()
    return macKeyPairSHA3_256Str
if __name__ == "__main__":
    restore_dict()
    sio.connect('http://'+sys.argv[1]+':5000')
    if len(sys.argv)==6:
        if sys.argv[2]=="-add":
            add_pair(sys.argv[3],sys.argv[4],sys.argv[5])
        if sys.argv[2]=="-remove":
            remove_pair(sys.argv[3],sys.argv[4],sys.argv[5])
    sio.wait()

