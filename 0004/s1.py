import socket

# Create a TCP/IP socket
sock = socket.socket()

# Get local machine name
host = socket.gethostname()
host = socket.gethostname()

port = 9999
# print('starting up on {} port {}'.format(*server_address))
# server_socket.bind((host, port))
sock.bind((host, port))
print(f'Listening for incoming connections on {host}:{port}...')
# Listen for incoming connections
sock.listen(1)

# Dictionary of names and ages
names_ages = {
    "Alice": 25,
    "Bob": 30,
    "Eve": 35
}

# Dictionary to store client data
client_data = {}

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive data from the client
        data = connection.recv(1024)
        data = data.decode()
        print('received {!r}'.format(data))

        # Save the data in the client data dictionary
        client_data[client_address] = data

        # Check if the received data is a name in the names_ages dictionary
        if data in names_ages:
            age = names_ages[data]
            response = "Your age is {}. Do you want to search for another name? (y/n)".format(age)
        else:
            response = "Name not found. Do you want to search for another name? (y/n)"

        # Send the response to the client
        connection.sendall(response.encode())

        # Receive the response from the client
        data = connection.recv(1024)
        data = data.decode()

        # If the client wants to search for another name, start the process over again
        if data == "y":
            continue
        else:
            break
    finally:
        # Clean up the connection
        connection.close()
