# Client file
import socket
import threading

alias = input("Choose an alias >>> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

# Function to receive messages from the server
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Function to send messages to the server
def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

# Start the thread to receive messages
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

# Start the thread to send messages
send_thread = threading.Thread(target=client_send)
send_thread.start()
