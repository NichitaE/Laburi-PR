import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# socket udp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((UDP_IP, UDP_PORT))

try:
    print("Serverul este pregătit să primească mesaje...")

    while True:
        data, client_address = server_socket.recvfrom(1024)

        server_socket.sendto(b"Mesaj primit de la server.", client_address)

        print("Mesaj de la {}: {}".format(client_address, data.decode()))

finally:
    server_socket.close()
