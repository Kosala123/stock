import socket
import threading
import pandas as pd

df = pd.read_csv('stocks.csv')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))

server_socket.listen(5)

users = {"user1": "password1", "user2": "password2"}

stocks = {}


for _, row in df.iterrows():
    symbol = row['Symbol']
    price = row['Price']
    security = row['Security']
    profit = row['Profit']
    stocks[symbol] = {'Price': price, 'Security': security, 'Profit': profit}

def print_table(stocks):
    rows = []
    rows.append('Symbol\tPrice\tSecurity\tProfit')
    rows.append('-----------------------------')
    for symbol, info in stocks.items():
        rows.append(f'{symbol}\t{info["Price"]}\t{info["Security"]}\t{info["Profit"]}')
        table_string = '\n'.join(rows)
    return str(table_string)

def handle_client(client_socket, client_address):
    username = client_socket.recv(1024).decode("utf-8")
    password = client_socket.recv(1024).decode("utf-8")

    if username in users and users[username] == password:
        client_socket.send("Welcome!".encode("utf-8"))
        client_socket.send(print_table(stocks).encode("utf-8"))
    re = ""
    while True:
        try:
            re = client_socket.recv(1024).decode("utf-8")
        except:
            pass

        if re == "all":
            client_socket.send(print_table(stocks).encode("utf-8"))
        if re == "exit":
            break
        else:
            client_socket.send("Invalid login!".encode("utf-8"))

        client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print(f'New client connected from {client_address}')
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()