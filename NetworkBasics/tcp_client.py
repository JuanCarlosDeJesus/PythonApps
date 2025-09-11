#TCP client side
import socket

# Create a TCP/IP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# Receive the welcome message from the server - specify buffer size
welcome_message = client_socket.recv(1024)
print("Received:", welcome_message.decode())

# Close the client socket
client_socket.close()