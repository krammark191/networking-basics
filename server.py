import socket
import pickle

HEADER_SIZE = 10
PORT_NUMBER = 9999

host_name = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host_name, PORT_NUMBER))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print('Connected to', address)

    d = {1: "Hello", 2: "World", 3: "!"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg
    clientSocket.send(msg)