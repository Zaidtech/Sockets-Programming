#  this is a tcp server which will be sending the data from the client and also receiving it after 
# connection has been established

import socket   
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  server has a listen mode to hear for the new_connections to it
server_socket.bind(("192.168.1.7", 800))
#  the server has a bind method which binds it to a port and an ip so that it can listen to  requests 
# on that particular port and addrs.
server_socket.listen(5) #it is a limit of the no of connections 

while True:
    print("Server waiting for a connection")
    client_socket, addr = server_socket.accept()
    print("client connected from ", addr)
    while True:
        data = client_socket.recv(2048000)
        if not data: #--->
            break 
        print(f"From other side:-> ",data.decode("utf-8"))
        # print(f"Reeived Data form the client in the decoded form ", data.decode("utf-8"))
        try:
            msg = input("Enter your msg here:-> ")
            client_socket.send(bytes(msg, 'utf-8'))
        except:
            print("Exited by the user")
    client_socket.close()
server_socket.close()