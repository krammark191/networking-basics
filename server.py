import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print('Connected to', address)
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()