import socket

if __name__ == "__main__":
    # define the socket parameters
    host = '127.0.0.1'
    port = 8080
    totalClients = int(input("Enter number of clients to wait for: "))

    # create a ipv4 and TCP socket = socket.AF_INET, socket.SOCK_STREAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))  # bind the socket to the address
    sock.listen(totalClients)  # listen for incoming connections
    connections = []
    print(f"Server listening on {host}:{port}...")


    for i in range(totalClients):
        conn = sock.accept()
        connections.append(conn)
        print(f"Connection established with {i+1} client(s)")

    fileno = 0
    idx = 0
    for conn in connections:
        idx += 1
        data = conn[0].recv(1024).decode()  # receive data from the client
        if not data:
            continue
        filename = f"output {str(fileno)} .txt"
        fileno += 1
        with open(filename, 'w') as fo:
            while data:
                if not data:
                    break
                else:
                    fo.write(data)
                    data = conn[0].recv(1024).decode()  # receive data from the client
            print(f"\nReceiving file from client {idx}\n")
            print(f"File received from client {idx} and saved as {filename}\n")
        
    # close the socket connection
    for conn in connections:
        conn[0].close()