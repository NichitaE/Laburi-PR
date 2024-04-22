import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 5005


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Introdu mesajul: ")  
    
    
    if message.startswith("/p "):
        parts = message.split(" ", 2)
        if len(parts) == 3:
            recipient, private_message = parts[1:]
            client_socket.sendto(("MSG_PRIVATE:{}:{}".format(recipient, private_message)).encode(), (UDP_IP, UDP_PORT))
        else:
            print("Formatul mesajului privat este incorect.")
    else:
        client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))  

