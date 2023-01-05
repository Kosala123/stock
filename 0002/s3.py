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

# A dictionary to store the client number for each connection
client_numbers = {}

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f'Received connection from {address}')

    # Add the connection to the list of connections
    connections.append(connection)

    # Assign a unique number to the client
    client_number = len(client_numbers) + 1
    client_numbers[connection] = client_number

    while True:
        # Send a message to the client asking for information
        connection.send(b'Please provide some information:')

        # Receive the information from the client
        data = connection.recv(1024).decode()

        # Prefix the data with the client number
        data = f'[{client_number}] {data}'

        # Send the received data back to the client
        connection.send(data.encode())

# Close the connections
for conn in connections:
    conn.close()
