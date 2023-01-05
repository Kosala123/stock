import socket
from _thread import *
serversocket = socket.socket()

host = "127.0.0.1"
port = 2021
ThreadCount = 0
password_cheak=[]
try:
    serversocket.bind((host,port))
except socket.error as e:
    print(str(e))
print("waiting for connection")
serversocket.listen(5)

def client_thread(connection):
    connection.send(str.encode("welcome to the Stock Market"))
    while True:
        data = connection.recv(2048)
        kosa="Enter your password: "
        connection.send(str.encode(kosa))
        data_1= connection.recv(2048)
        data_2 = data_1.decode("utf-8")

        password_cheak.append(data_2)
        password_cheak_1 = len(password_cheak[0])
        print(password_cheak_1)
        if password_cheak_1 == 8:
            password_cheak.clear()

            password_cheak_2 = "Correct Password"
            connection.send(str.encode(password_cheak_2))
        else:
            password_cheak_3 = "InCorrect Password"
            connection.send(str.encode(password_cheak_3))

    connection.close()



while True:
    client,address = serversocket.accept()
    print("connect to"+address[0]+str(address[1]))
    start_new_thread(client_thread,(client,))
    print("ThreadNumber"+str(ThreadCount))
serversocket.close()


