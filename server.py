import socket
import pickle

# Set constant values.
HEADER_SIZE = 10    # Size of the header.
PORT_NUMBER = 9999  # Port number of the server.

# Grabs the IP address that the server is located
# on and stores it in the host_name variable.
host_name = socket.gethostbyname(socket.gethostname())

# Creates a socket object and binds the server
# to the local IP address and sets the port number.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object.
s.bind((host_name, PORT_NUMBER))                        # Bind to the server.
s.listen(5)                                             # Listen for connections.

# Begins send loop.
while True: # Loop forever.

    # Connects to any client requests and saves the values.
    clientSocket, address = s.accept()  # Accept a connection.

    # Prints confirmation message that a
    # client is connected and prints the address.
    print('Connected to', address)  # Prints the address of the client.

    # Creates a python object. This is arbitrary.
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
    msg = pickle.dumps(d)   # Compress the python object.

    # Converts the message header to byte format and appends the pickle object.
    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg    # Convert the header to a string.

    # Sends the message to the client.
    clientSocket.send(msg)  # Send the message.