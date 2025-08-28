import socket

# create socket
s = socket.socket()

# set up port
port = 56789

# connect to server
s.connect(('127.0.0.1', port))  # connect to localhost

# receive message
message = s.recv(1024).decode()  # .decode() converts bytes to string
print(f"Message from server: {message}")

# close socket
s.close()