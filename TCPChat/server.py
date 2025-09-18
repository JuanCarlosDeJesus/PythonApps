# TCP chat connection 
import socket
import threading  # to handle multiple clients

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
server.bind((host, port))
server.listen(5)

# Lists for clients and their aliases
clients = []
aliases = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients' connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)  # 1024 - max amount a client can recieve
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat.'.encode('utf-8'))
            aliases.remove(alias)
            break


# Main function to receive the clients connection
def receive():
    while True:
        print("Server is running and listening ...")
        client, address = server.accept()
        print(f"Connection is established with {str(address)}")
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'Alias of the client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat.'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# Main function
if __name__ == "__main__":
    receive()