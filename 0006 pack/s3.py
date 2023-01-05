from itertools import count
import socket
import threading
import pandas as pd

# Read the CSV file
df = pd.read_csv('stocks.csv')




# Create a socket and bind it to a host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))

# Start listening for incoming connections
server_socket.listen(5)

# A dictionary to store usernames and passwords
users = {"user1": "password1", "user2": "password2"}

# Create a dictionary to store the data
stocks = {}

global c_num
c_num = 0


# Loop through the rows and store the data in the dictionary
for _, row in df.iterrows():
    symbol = row['Symbol']
    price = row['Price']
    security = row['Security']
    profit = row['Profit']
    stocks[symbol] = {'Price': price, 'Security': security, 'Profit': profit}

# # Print the data
# print(stocks)
def print_table(stocks):
    # Create a list of strings representing each row in the table
    rows = []
    
    # Add the table header to the list
    rows.append('Symbol\tPrice\tSecurity\tProfit')
    rows.append('-----------------------------')
    
    # Add the information for each stock to the list
    for symbol, info in stocks.items():
        rows.append(f'{symbol}\t{info["Price"]}\t{info["Security"]}\t{info["Profit"]}')
    
    # Use the join method to combine the rows into a single string
    table_string = '\n'.join(rows)
    
    # Print the table
    return str(table_string)

# Print the table
############print(print_table(stocks))

def handle_client(client_socket):
  while True:
    # Receive the client's login credentials
    username = client_socket.recv(1024).decode("utf-8")
    password = client_socket.recv(1024).decode("utf-8")

    # Check if the provided credentials are correct
    if username in users and users[username] == password:
      client_socket.send("Welcome!".encode("utf-8"))
      # Send the dictionary with information about the people
      client_socket.send(print_table(stocks).encode("utf-8"))
      re = ""
      while True:
            re = client_socket.recv(1024).decode("utf-8")
            if re == "all":
                client_socket.send(print_table(stocks).encode("utf-8"))
            elif re == "exit":
                break
            else:
                client_socket.send("Invalide command".encode("utf-8"))
        
      break
    else:
      client_socket.send("Invalid login!".encode("utf-8"))
  # Close the client socket
  client_socket.close()

while True:
  # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f'New client connected from {client_address}')
  # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
