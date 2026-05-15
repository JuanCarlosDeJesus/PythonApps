import socket


if __name__ == "__main__":
    # define the socket parameters
    host = '127.0.0.1'
    port = 8080

    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    sock.connect((host, port))

    # send data to the server
    while True:
        filename = input("Enter the filename to send: ")
        try:
            with open(filename, 'rb') as fi:
                data = fi.read()
                if not data:
                    break
                while data:
                    sock.send(str(data).encode())
                    data = fi.read()
                fi.close()
        except IOError:
            print("You entered an invalid filename. Please try again.")

    # close the socket
    sock.close()