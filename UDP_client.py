import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hellow client here"
client_sock.sendto( msg.encode('utf-8'), ('127.0.0.1', 12345) )
data , addr = client_sock.recvfrom(4096)
print("Server send : ", data.decode('utf-8'))

client_sock.close()