# TCP server side
import socket

# Create a TCP/IP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# See how to get ip address of the machine
# print("Hostname:", socket.gethostname())
# print("Server IP address:", socket.gethostbyname(socket.gethostname()))

# Bind the socket to the address and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Listen for incoming connections
server_socket.listen()
print("Server listening on port 12345")

# Listen for incoming connections
while True:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    # print(type(client_socket))
    # print(client_socket)
    # print(type(addr))
    # print(addr)
    print(f"Connected to {addr[0]}:{addr[1]}\n")

    # Send a welcome message
    client_socket.send("Hello from server".encode())

    # Close the client socket
    client_socket.close()
    break