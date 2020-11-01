#!/usr/bin/env python3
import socket
import sys

# basically 90% of internet stuff  is done using the AF_INET class 
try:    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Fail to create a socket ")
    sys.exit()

print("Socket created")

target_host  = input("Enter the target host name to connect: ")
target_port  = input("Enter the target port: ")

try:    
    sock.connect((target_host, int(target_port)))
    print("Socket connected")
    sock.shutdown(2)
except socket.error as err:
    print(f"Fail to connect to {target_host} at port no {target_port} due to {err}")

