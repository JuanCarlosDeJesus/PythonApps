# This program will help you find available WiFi networks and connect to them.
import subprocess

nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
decoded_nw = nw.decode('ascii')
print(decoded_nw)