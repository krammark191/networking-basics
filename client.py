import socket
import pickle

# Set constant values.
HEADER_SIZE = 10    # Size of the header.
PORT_NUMBER = 9999  # Port number of the server.
SERVER_IP = '10.36.37.83' # Replace with server IP address.

# Open a socket and connect to the server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object.

# The first parameter should be SERVER_IP for network connection, or socket.gethostname() for local connection.
s.connect((socket.gethostname(), PORT_NUMBER))          # Connect to the server.


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
            print(f"new message length: {msg[:HEADER_SIZE]}")   # Display the header.
            msg_length = int(msg[:HEADER_SIZE])                 # Convert the header to an integer.

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
            new_msg = True  # Set new_msg to True as it is now the first buffer of the next message.
            full_msg = b''  # Reset full_msg to empty.