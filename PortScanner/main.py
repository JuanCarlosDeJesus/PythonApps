# Simple Port Scanner using nmap library
# Make sure to install the nmap library using: pip install python-nmap

# !!!!! WARNING !!!!!
# Scanning ports on systems you do not own or have explicit permission to scan is illegal and unethical.
# Always ensure you have permission before performing any port scanning activities.

# Run via command line: python main.py!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

import nmap

# port scanning from 75 to 80 on localhost
begin =  75
end = 80
target = '127.0.0.1'

# port scanning object
scanner = nmap.PortScanner()
for i in range(begin, end + 1): # inclusive range of ports
    res = scanner.scan(target, str(i)) # scan localhost + port i
    res = res['scan'][target]['tcp'][i]['state'] # get open ports
    print(f'Port {i} is {res}')