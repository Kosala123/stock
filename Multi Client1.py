import socket

# Create a socket object
client_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 2021

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
client_socket.send(b'Hello, server!')

# Receive data from the server
data = client_socket.recv(1024).decode()

print(f'Received data from the server: {data}')

# Close the connection
client_socket.close()
