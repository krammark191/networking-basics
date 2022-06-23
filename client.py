import socket
import pickle

# Set constant values.
HEADER_SIZE = 10
PORT_NUMBER = 9999
SERVER_IP = '10.36.37.83' # Replace with server IP address.

# Open a socket and connect to the server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT_NUMBER))


while True:

    # Initialize full_msg and new_msg variables.
    full_msg = b''
    new_msg = True

    # Begin receive loop.
    while True:

        # Set buffer size of 16 bytes.
        msg = s.recv(16)

        # Checks if their is still information to be received.
        if new_msg:

            # Display the header and the message size.
            print(f"new message length: {msg[:HEADER_SIZE]}")
            msg_length = int(msg[:HEADER_SIZE])

            # Set new_msg to False as it is no longer the first buffer of the message.
            new_msg = False

        # Add the first buffer of the message to the full message.
        full_msg += msg

        # Checks to see if the message is fully received.
        if len(full_msg) - HEADER_SIZE == msg_length:

            # Prints confirmation of message received.
            print("full msg recvd")
            print(full_msg[HEADER_SIZE:])

            # Decrypts pickle message from byte format to python object.
            d = pickle.loads(full_msg[HEADER_SIZE:])

            # Prints the decrypted message.
            print(d)

            # Sets variables back to their default states and awaits the next message.
            new_msg = True
            full_msg = b''