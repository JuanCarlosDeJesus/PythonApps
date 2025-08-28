import socket


s = socket.socket()
print("Socket successfully created")

port = 56789
s.bind(('', port))  # leave the IP blank to bind to all interfaces
print(f"Socket bound to port {port}")

# socket on listening
s.listen(5) # no. of connections
print("Socket is listening...")

while True:
    c, addr = s.accept()
    print(f"Connection established with {addr}")
    message = "Thank you for connecting"
    c.send(message.encode())  # .encode() converts the string message to bytes
    c.close()