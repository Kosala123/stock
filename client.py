import socket

clientsocket = socket.socket()

host = "127.0.0.1"
port = 2021

print("waiting for connection")

try:
    clientsocket.connect((host,port))
except socket.error as e:
    print(str(e))

Response = clientsocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    client_1 = input(str("Enter your User name:"))
    clientsocket.send(str.encode(client_1))
    resource = clientsocket.recv(1024)
    print(resource.decode("utf-8"))
    client_2 = input()
    clientsocket.send(str.encode(client_2))
    password_cheak_two = clientsocket.recv(1024)
    print(password_cheak_two.decode("utf-8"))

clientsocket.close()
