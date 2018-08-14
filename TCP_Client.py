import socket
import time


def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent

def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk.decode()
    return msg

serv = input("Enter server number:")
mes = 1


while True:
    req = ("Message: "+str(mes)+" from Server: "+str(serv)).encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    s.send(req)
    rsp = s.recv(1024).decode()
    #mysend(s,req)
    #rsp = myreceive(s,1024)
    s.close()
    print(rsp)
    mes = mes + 1
    time.sleep(2)