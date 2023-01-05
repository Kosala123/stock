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


class Stock:

    def __init__(self, symbol, price, security, profit):
        self.symbol = symbol
        self.price = price
        self.security = security
        self.profit = profit






stocks = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 35,
    'Dave': 40,
    'Eve': 45,
    'Frank': 50,
    'Gina': 55,
    'Hannah': 60,
    'Igor': 65,
    'Jack': 70
}