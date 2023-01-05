from threading import Thread
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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a list of 10 people
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 35),
    Person('Dave', 40),
    Person('Eve', 45),
    Person('Frank', 50),
    Person('Gina', 55),
    Person('Hannah', 60),
    Person('Igor', 65),
    Person('Jack', 70)
]



def handle_client():
    while True:
        connection, address = server_socket.accept()
        # Send a message to the client asking for information
        connection.send(b'Please provide some information:')

        # Receive the information from the client
        data = connection.recv(1024).decode()

        if data == "all":
            connection.send("AAAA".encode())
            connection.send("Name     Age\n".encode())
            for i in people:
                connection.send(f"{i.name}    {i.age}".encode())

            connection.send("done".encode())

        person = None
        for p in people:
            if p.name == data:
                person = p
                break
        # Prefix the data with the client number
        if person is not None:
            data = f'[{client_number}] {person.age}'
            connection.send(data.encode())
        else:
            connection.send(b'None')
        # Send the received data back to the client


while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print(f'Received connection from {address}')

    # Add the connection to the list of connections
    connections.append(connection)

    # Assign a unique number to the client
    client_number = len(client_numbers) + 1
    client_numbers[connection] = client_number

    # Start a new thread to handle the incoming connection
    thread = Thread(target=handle_client, args=(connection, client_number))
    thread.start()
# Close the connections


for conn in connections:
    conn.close()
