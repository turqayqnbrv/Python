import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return True
    except:
        return False

host = input("Enter the host to scan: ")

for port in range(1, 65535):
    if port_scanner(host, port):
        print("Port", port, "is open")
