import socket
from threading import Thread

# definim Ip si portul
host = "localhost"
port = 8080

clients = {}

# crearea unui socket object 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((host, port))


# functia pentru a primi numele 
def handle_clients(conn):
    name = conn.recv(1024).decode()
    welcome = f"Welcome {name}. Good to see you :)"
    conn.send(bytes(welcome, "utf8"))
    msg = name + " has recently joined us"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name
    while True:
        msg = conn.recv(1024)
        broadcast(msg, name + ":")


# functia pentru a transmite mesajul la toti 
def broadcast(msg, prefix=""):
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)

#in functia data acceotptam userii care se conecteaza si le trimitem un mesaj 
def accept_client_connection():
    while True:  
        client_conn, client_address = sock.accept()  
        print(client_address, " has Connected")

        
        client_conn.send(bytes("Welcome to the chat room, Please type your name to continue", "utf8"))

       
        Thread(target=handle_clients, args=(client_conn,)).start()


if __name__ == "__main__":
    sock.listen(3)  # acceptam 3 conectari 
    print("listening on port : ", port, "......")
    
    t = Thread(target=accept_client_connection)

    t.start()  
    t.join()
