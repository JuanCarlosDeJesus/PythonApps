# Camera Chat
from vidstream import StreamingServer
from vidstream import CameraClient

import threading
import time

receiving = StreamingServer('192.168.56.1', 9999) # myip.is 222.127.93.32 public address
sending = CameraClient('192.168.254.196', 9999) # laptop addy

t1 = threading.Thread(target=receiving.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target=sending.start_stream)
t2.start()

while input("") != "STOP":
    continue

receiving.stop_server()
sending.stop_stream()
