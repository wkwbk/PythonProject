import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for data in [b'Tom', b'Jerry', b'Spike']:
    s.sendto(data, ('127.0.0.1', 6666))
    print(s.recv(1024).decode('utf-8'))
    s.close()
