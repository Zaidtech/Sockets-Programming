# to solve the problem of concurency 
# handling multiple clients using the thread module in python
#  for two clients

import socket
from _thread import *

server_socket = socket.socket()

HOST = '127.0.0.1'
PORT = 1233

thread_count = 0

try:
    server_socket.bind((HOST, PORT))
except socket.error as err:
    print(err)
print("Waiting for a  connection")
server_socket.listen(5)
# that handles diff clients 
def client_thread(connection):
    connection.send(str.encode("Welcome to the server"))
    while True:
        data = connection.recv(2048)
        reply = "Hellow, I am a server "+ data.encode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client, address = server_socket.accept()
    print(f"connected to {address[0]} - {str(address[1])}") 
    start_new_thread(client_thread, (client, ))
    thread_count+=1
    print(f"No of servers connected are {thread_count}")
server_socket.close()





