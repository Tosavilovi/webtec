import os
import sys
import socket

s = socket.socket()
s.bind(('127.0.0.1', 1234))
s.listen(10)

while True:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
        conn.close()
        sys.exit()
    else:
        conn.close()

s.close()