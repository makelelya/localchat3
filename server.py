import socket
import threading

PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)

FORMAT = "utf-8"

clients, names = [], []

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(ADDRESS)


def startChat():
    print("Сервер активен: " + SERVER)

    server.listen()

    while True:
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))

        name = conn.recv(1024).decode(FORMAT)

        names.append(name)
        clients.append(conn)

        thread = threading.Thread(target=handle,
                                  args=(conn, addr))
        thread.start()


def handle(conn, addr):
    connected = True

    while connected:
        message = conn.recv(1024)

        broadcastMessage(message)

    conn.close()


def broadcastMessage(message):
    for client in clients:
        client.send(message)




startChat()