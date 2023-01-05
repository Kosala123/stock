import socket

# Create a socket object
server_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 2021

# Bind to port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen()

print(f'Listening for incoming connections on {host}:{port}...')

# A list to keep track of client connections
connections = []

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f'Received connection from {address}')

    # Add the connection to the list of connections
    connections.append(connection)

    # Receive data from the connection
    data = connection.recv(1024).decode()

    # Send the data to all of the clients
    for conn in connections:
        conn.send(data.encode())

# Close the connections
for conn in connections:
    conn.close()
