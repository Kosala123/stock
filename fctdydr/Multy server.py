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

# A list to keep track of client connections
connections = []

# A dictionary to store the username and password for each client
client_auth = {}

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f'Received connection from {address}')

    # Add the connection to the list of connections
    connections.append(connection)

    # Receive the username and password from the client
    username = connection.recv(1024).decode()
    password = connection.recv(1024).decode()

    # Store the username and password in the client_auth dictionary
    client_auth[connection] = (username, password)

    # Send a message to the client indicating whether the login was successful
    if (username, password) in client_auth.values():
        connection.send(b'Success')
    else:
        connection.send(b'Failure')

# Close the connections
for conn in connections:
    conn.close()
