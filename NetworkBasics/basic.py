# Socket Programming Basics
import socket
import sys

try:
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = ipv4 ip protocl 4 ; SOCK_STREAM = TCP
    print("Socket Created")
except socket.error as err:
    print(f"Socket Creation Failed: {err}")
    sys.exit()

# Default port for socket
port = 80

try:
    # get ip for website - using .gethostbyname()
    host_ip = socket.gethostbyname(input("Enter Hostname to connect: ")) # e.g. www.google.com
except socket.gaierror: # problem with DNS
    print("Hostname could not be resolved.")
    sys.exit()

# Connect to server
s.connect((host_ip, port))
print(f"Socket Connected to www.google.com on ip {host_ip} and on port: {port}")