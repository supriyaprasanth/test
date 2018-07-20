#printing ip address and current date and time

import socket
import datetime

#to display the ip addrss
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("The IP Address is:" + IPAddr)

#to disp the cur date and time
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print('\n');
