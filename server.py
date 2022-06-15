import socket
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print('Connected to', address)

    d = {1: "Hello", 2: "World"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg
    clientSocket.send(msg)