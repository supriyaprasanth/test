import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Hostname :  ", host_name)
print("IP : ", host_ip)
