import socket
import pickle

# Set constant values.
HEADER_SIZE = 10
PORT_NUMBER = 9999

# Grabs the IP address that the server is located
# on and stores it in the host_name variable.
host_name = socket.gethostbyname(socket.gethostname())

# Creates a socket object and binds the server
# to the local IP address and sets the port number.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host_name, PORT_NUMBER))
s.listen(5)

# Begins send loop.
while True:

    # Connects to any client requests and saves the values.
    clientSocket, address = s.accept()

    # Prints confirmation message that a
    # client is connected and prints the address.
    print('Connected to', address)

    # Creates a python object.
    d = {"Test 1": [1, 2, 3, 4, 5],
         "Test 2": [
        5, 4, 3, 2, 1],
        "Test 3": True,
        "Test 4": False,
        "Test 5": 5,
        "Test 6": 6.0,
        "Test 7": {1: 1, 2: 2, 3: 3}}

    # Compresses the python object into a
    # sendable format with the pickle library.
    msg = pickle.dumps(d)

    # Converts the message header to byte format and appends the pickle object.
    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg

    # Sends the message to the client.
    clientSocket.send(msg)