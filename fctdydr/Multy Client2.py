import socket

# Create a socket object
client_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 9999

# Connect to the server
client_socket.connect((host, port))

# Send the username and password to the server
username = input('Enter your username: ')
client_socket.send(username.encode())
password = input('Enter your password: ')
client_socket.send(password.encode())

# Receive the login response from the server
response = client_socket.recv(1024).decode()

if response == 'Success':
    print('Login successful!')
else:
    print('Login failed')

# Close the connection
client_socket.close()
