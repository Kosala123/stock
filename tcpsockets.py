import socket
import sys
try:
    sock=socket.socket(socket.AF_INET.socket.SOCK_STREAM)
except socket.error as err:
    print("failed to create a socket")
    print("Reason"+str(err))
    sys.exit()
print('socket created')

target_host=input("Enter the target_host name to connect")
target_port=input ("Enter the target port")
try:
    sock.connect(target_host(target_port))
    print("socket connect to:"+target_host+target_port)
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect"+ target_host+target_port)
    print("reason"+str(err))
    sys.exit()
    
