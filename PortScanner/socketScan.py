# Simple Port Scanner using nmap library
# Make sure to install the nmap library using: pip install python-nmap

# Port information - in in Layer 2 of OSI model
# Ports are used to identify specific processes or services on a device.
# TCP and UDP
# from 0 to 65535 (0-1023: well-known ports, 1024-49151: registered ports, 49152-65535: dynamic/private ports)

# !!!!! WARNING !!!!!
# Scanning ports on systems you do not own or have explicit permission to scan is illegal and unethical.
# Always ensure you have permission before performing any port scanning activities.

# Run via command line: python main.py!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
from socket import *
import time

starttime = time.time()

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    t_ip = gethostbyname(target)
    print(f'Scanning target: {t_ip}')

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM) # TCP

        conn = s.connect_ex((t_ip, i)) # returns an error indicator
        if conn == 0:
            print(f'Port {i} is open')
        s.close()
    print(f'Scanning completed in: {time.time() - starttime} seconds')
