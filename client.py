import socket
import pickle

HEADER_SIZE = 10
PORT_NUMBER = 9999
SERVER_IP = '10.244.37.20' # Replace with server IP address.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT_NUMBER))


while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADER_SIZE]}")
            msg_length = int(msg[:HEADER_SIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg) - HEADER_SIZE == msg_length:
            print("full msg recvd")
            print(full_msg[HEADER_SIZE:])
            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)
            new_msg = True
            full_msg = b''
