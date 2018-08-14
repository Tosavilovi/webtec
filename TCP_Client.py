import socket
import time



#serv = input("Enter server number:")
mes = 1


while True:
    req = ("Message: "+str(mes)+" from client 1 ").encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    s.send(req)
    rsp = s.recv(1024).decode()
    #s.close()
    print(rsp)
    #mes = mes + 1
    #time.sleep(2)

    req = ("Message: " + str(mes) + " from client 2 ").encode()
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect(('127.0.0.1', 1234))
    s1.send(req)
    rsp = s1.recv(1024).decode()
    print(rsp)
    mes = mes + 1
    time.sleep(2)

    s1.close()
    s.close()