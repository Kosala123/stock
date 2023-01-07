import socket
import threading
import pandas as pd
import time

#Read the CSV file
df = pd.read_csv('stocks.csv')

#bind the socket to a host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))

#Start listening for incoming connections
server_socket.listen(5)

#Create a dictionary to store the data
stocks = {}

#store the data in the dictionary
for _, row in df.iterrows():
    symbol = row['Symbol']
    price = row['Price']
    security = row['Security']
    profit = row['Profit']
    stocks[symbol] = {'Price': price, 'Security': security, 'Profit': profit}

# Print the data and print(stocks)
def print_table(stocks):
    #Create a list of strings
    rows = []
    
    #Add the data and append table header to the list
    rows.append('_____________________________')
    rows.append('Symbol\tPrice\tSecurity\tProfit')
    rows.append('-----------------------------')
    
    #Add the information for each stock to the list
    for symbol, info in stocks.items():
        rows.append(f'{symbol}\t{info["Price"]}\t{info["Security"]}\t\t{info["Profit"]}')
    
    #Use the join method to combine the rows into a single string
    table_string = '\n'.join(rows)
    
    #Print the table
    return str(table_string+"\n\n")


#A dictionary to store usernames and passwords
users = {"user1": "password1", "user2": "password2","user3": "password3", "user4": "password4", "1": "1"}

#Print the table
def handle_client(client_socket):
  while True:
    #Receive the input data and client's log
    username = client_socket.recv(1024).decode("utf-8")
    password = client_socket.recv(1024).decode("utf-8")

    #Check the username and password 
    if username in users and users[username] == password:
      client_socket.send("Welcome!".encode("utf-8"))
      # Send the dictionary with information about the people
      client_socket.send(print_table(stocks).encode("utf-8"))

      #create new String
      recive_string = ""
      while True:
            recive_string = client_socket.recv(1024).decode("utf-8")
            if recive_string == "Buy":
              input_data = print_table(stocks)+"\nPlease select the symbol"
              client_socket.send((input_data).encode("utf-8"))
              while True:
                input_data_1 = client_socket.recv(1024).decode("utf-8")
                if input_data_1 == "Back":
                  client_socket.send("Bid another item".encode("utf-8"))
                  break
                if input_data_1 in stocks:
                  name = f"\n\nCurrent price of {input_data_1} is " +str(stocks[input_data_1]["Price"])+"\nEnter your bid\nType Back to change company\n\n"
                  client_socket.send(name.encode("utf-8"))
                  recive_string = client_socket.recv(1024).decode("utf-8")
                  try:
                    bid = float(recive_string)
                    if bid > stocks[input_data_1]["Price"]:
                      stocks[input_data_1]["Price"] = bid
                      biddone = f"\n\n        ***Bid Done*** \n\n{print_table(stocks)}\n"
                      client_socket.send(biddone.encode("utf-8"))
                    else:
                      client_socket.send("Bid is to small...".encode("utf-8"))

                  except ValueError:
                    if recive_string == "Back" or recive_string == "exit":
                      client_socket.send("okey".encode("utf-8"))
                      if recive_string == "exit":
                        break
                    else:
                      client_socket.send("Invalide Symbol".encode("utf-8"))
                      
        
                else:
                  client_socket.send("Invalide Symbol".encode("utf-8"))

            elif recive_string == "exit":
                break #logout
            else:
                client_socket.send("Invalide Request".encode("utf-8"))
        
      break #final exit
    else:
      client_socket.send("Enter the Correct Username and Password!!".encode("utf-8"))
  #Close the client socket
  client_socket.close()

while True:
  #Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f'New client connected from {client_address}')

  #Start a new thread to handle the client
    create_client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    create_client_thread.start()