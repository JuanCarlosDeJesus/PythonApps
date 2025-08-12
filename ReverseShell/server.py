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

        print("Binding the port " + str(port))

        s.bind((host, port))  # .bind is a socket method thats a tuple
        s.listen(5)  # allow 5 connections
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        Bind_socket()  # if error, try again