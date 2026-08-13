import socket
import sys
from datetime import datetime

# Target Definition
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 port_scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    # Scan ports between 1 and 100
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname Could Not Be Resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
