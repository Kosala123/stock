import socket

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8080))

# Send the login credentials
username = input("Enter your username: ")
password = input("Enter your password: ")
client_socket.send(username.encode("utf-8"))
client_socket.send(password.encode("utf-8"))

# Receive the response from the server
response = client_socket.recv(1024).decode("utf-8")
print(response)

# Close the socket
client_socket.close()
