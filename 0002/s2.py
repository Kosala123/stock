import socket

# Create a socket object
server_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 9999

# Bind to port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen()

print(f'Listening for incoming connections on {host}:{port}...')

# Accept an incoming connection
connection, address = server_socket.accept()
print(f'Received connection from {address}')

while True:
    # Send a message to the client asking for information
    connection.send(b'Please provide some information:')

    # Receive the information from the client
    data = connection.recv(1024).decode()

    # Send the received data back to the client
    connection.send(data.encode())

# Close the connection
connection.close()
