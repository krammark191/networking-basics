# Overview

This networking program has a server and a client. The server, when prompted by a client, will return a python object. Multiple clients could be set up, the server, when asked, will always return the same thing. Code could be modified to create a menu system in the client that then asks the server for a specific response.

My purpose for writing this software was to learn the basics of networking. Now that I know how to have a client talk to a server, I can expand my programs to create a file system or a client-to-client chat system through the server.

[Software Demo Video](https://youtu.be/wpmBe6jMMe4)

# Network Communication

I used a client/server architecture.

I used UDP and Port Number 9999, although the port number is arbitrary.

Messages are sent from the server to the client in byte format.

# Development Environment

## Tools
* Visual Studio Code
* Python IDLE

## Languages and libraries
* Python
* socket library (For the actual networking)
* pickle library (For converting and decoding python objects to and from byte format)

# Useful Websites

* [W3 Schools](https://www.w3schools.in/python/network-programming)
* [Python.org](https://docs.python.org/3/library/socket.html)

# Future Work

* Add another client
* Add multiple messages that can be sent from the server
* Create a chat system between two clients through the server
