import socket

client_socket = socket.socket()

HOST = '127.0.0.1'
PORT = 1233
 
try:
    client_socket.connect((HOST,PORT))
except:
    print("Error occured in connecting ")

Response =client_socket.recv(1024)
print(Response.decode('utf-8')) 
while True:
    msg = input("Enter the msg")
    client_socket.send(str.encode(msg))
    responce = client_socket.recv(1024)
    print(responce.decode('utf-8'))

client_socket.close()
 