import socket

# Create a socket object
client_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 9999

# Connect to the server
client_socket.connect((host, port))

while True:
    # Receive the message from the server
    message = client_socket.recv(1024).decode()
    if message == "AAAA":
        while message != "done":
            message = client_socket.recv(1024).decode()
            print(message)

    print(message)

    # Provide the requested information to the server
    information = input('Enter the requested information: ')
    client_socket.send(information.encode())

    # Receive the information from the server
    data = client_socket.recv(1024).decode()

    print(f'Received data from the server: {data}')

# Close the connection
client_socket.close()
