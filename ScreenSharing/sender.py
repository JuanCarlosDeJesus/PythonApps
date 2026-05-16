from vidstream import StreamShareClient
import threading

sender = ScreenShareClient('192.168.100.232', 9999)

t = threading.Thread(target=sender.start_server)
t.start()

while input("") != 'STOP':
    continue

sender.stop_server()