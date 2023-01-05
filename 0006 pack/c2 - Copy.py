import socket

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8080))

while True:
  # Send the login credentials
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  client_socket.send(username.encode("utf-8"))
  client_socket.send(password.encode("utf-8"))

  # Receive the response from the server
  response = client_socket.recv(1024).decode("utf-8")

  # If the login was successful, break out of the loop
  if response == "Welcome!":
    break
  else:
    print(response)

# Receive the dictionary with information about the people
people_str = client_socket.recv(1024).decode("utf-8")
#people = eval(people_str)
print(people_str)

user_input = ""

while user_input != "exit":
  # Send user input to the server and receive the response
  user_input = input(">>>")
  client_socket.send(user_input.encode("utf-8"))
  response = client_socket.recv(1024).decode("utf-8")
  print(response)

# Close the socket
client_socket.close()
