import socket

# Create a TCP/IP socket
sock = socket.socket()

# Get local machine name
host = socket.gethostname()
host = socket.gethostname()

port = 9999
sock.connect((host, port))

while True:
    # Prompt the user to enter a name
    name = input("Enter a name: ")

    try:
        # Send the name to the server
        print('sending {!r}'.format(name))
        sock.sendall(name.encode())

        # Receive data from the server
        data = sock.recv(1024)
        data = data.decode()
        print('received {!r}'.format(data))

        # Prompt the user to enter y or n
        response = input(data)

        # Send the response to the server
        sock.sendall(response.encode())

    except:
        pass