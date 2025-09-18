# UDP client side
import socket

# Create a UDP socket using IPv4 (AF_INET) and UDP (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server via UDP - connectionless protocol
client_socket.sendto("Hello from client".encode("utf-8"), (socket.gethostbyname(socket.gethostname()), 12345))
