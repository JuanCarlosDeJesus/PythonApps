# UDP Server side
import socket

# Create a UDP socket using IPv4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# We are not listening for connections in UDP, just waiting for data
message, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
print(f"Received message: {message.decode('utf-8')} from {addr[0]}:{addr[1]}")
