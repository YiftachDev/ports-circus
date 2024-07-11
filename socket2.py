import socket
import utils

ips = ["0.0.0.0", "127.0.0.1"]
port = 8821

ip_index = 1
status = "client"
client_msg = ""
while True:
    if status == "server":
        ip_index = 0
        server_socket = socket.socket()
        server_socket.bind((ips[ip_index], int(port)))
        server_socket.listen()
        (client_socket, client_addr) = server_socket.accept()
        client_msg_length = int(client_socket.recv(2).decode())
        client_msg = client_socket.recv(client_msg_length).decode()
        port = client_socket.recv(4).decode()
        print("Disconnecting...")
        server_socket.close()
        client_socket.close()
        status = "client"
        ip_index = 1
    if status == "client":
        client_socket = socket.socket()
        client_socket.connect((ips[ip_index], int(port)))
        if client_msg != "":
            print(client_msg)
        message_content = input("Message: ")
        port = input("Port: ")
        message = f"{str(len(message_content)).zfill(2)}{message_content}{port}"
        client_socket.send(message.encode())
        if message_content == "exit":
            break
        client_socket.close()
        status = "server"
        ip_index = 0

