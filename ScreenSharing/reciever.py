# Screen Sharing
from vidstream import StreamingServer
import threading

receiver = StreamingServer('192.168.56.1', 9999)  # your local ip addy

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()



