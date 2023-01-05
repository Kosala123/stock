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
# Listen for incoming connections
sock.listen(1)

# Dictionary of names and ages
names_ages = {
    "Alice": 25,
    "Bob": 30,
    "Eve": 35
}

# Dictionary to store usernames and passwords
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Dictionary to store client data
client_data = {}

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the username from the client
        username = connection.recv(1024)
        username = username.decode()

        # Check if the username is in the users dictionary
        if username in users:
            # Send a message to the client asking for a password
            connection.sendall("Enter password: ".encode())

            # Receive the password from the client
            password = connection.recv(1024)
            password = password.decode()

            # Check if the password is correct
            if password == users[username]:
                # Send a message to the client saying that the login was successful
                connection.sendall("Login successful".encode())

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
            else:
                # Send a message to the client saying that the password was incorrect
                connection.sendall("Incorrect password".encode())
        else:
            # Send a message to the client saying that the username was not found
            connection.sendall("Username not found".encode())
    finally:
        pass
# Clean
