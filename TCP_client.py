import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # takes the tuple of the address and the port no
while True:
    client_socket.connect(("172.31.26.173", 8080))

payload = "Hey server"

try:
    while True:
        client_socket.send(payload.encode("utf-8"))
        data = client_socket.recv(2048000)
        print(f" Received :", data.decode("utf-8"))
        payload = input("Enter your msg-> ")
except:
    pass