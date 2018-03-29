import socket
import sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)

def currect_connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data or b'close' in data:
            break
        conn.send(data)
    conn.close()
    sys.exit()

while True:
    conn, addr = s.accept()
    cur_thread = threading.Thread(target = currect_connection, args = (conn,addr))
    cur_thread.start()         
