import socket
import threading

# Create a socket and bind it to a host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))

# Start listening for incoming connections
server_socket.listen(5)

# A dictionary to store usernames and passwords
users = {"user1": "password1", "user2": "password2"}

# A dictionary with information about 3 people
people = {
  "person1": {"name": "Alice", "age": 30, "city": "New York"},
  "person2": {"name": "Bob", "age": 35, "city": "Chicago"},
  "person3": {"name": "Eve", "age": 25, "city": "San Francisco"},
}

def handle_client(client_socket):
  # Receive the client's login credentials
  username = client_socket.recv(1024).decode("utf-8")
  password = client_socket.recv(1024).decode("utf-8")

  # Check if the provided credentials are correct
  if username in users and users[username] == password:
    client_socket.send("Welcome!".encode("utf-8"))
    # Send the dictionary with information about the people
    client_socket.send(str(people).encode("utf-8"))
  else:
    client_socket.send("Invalid login!".encode("utf-8"))

  # Close the client socket
  client_socket.close()

while True:
  # Accept a new connection
  client_socket, client_address = server_socket.accept()

  # Start a new thread to handle the client
  client_thread = threading.Thread(target=handle_client, args=(client_socket,))
  client_thread.start()
