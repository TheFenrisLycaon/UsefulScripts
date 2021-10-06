import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

print(HOST)

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handleConnection(client):
    stop = 0
    while not stop:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception as e:
            index = clients.index(client)
            clients.remove(client)
            username = usernames[index]
            usernames.remove(username)
            broadcast(f"{username} has lest the chat!".encode('utf-8'))
            stop = 1

def main():
    print("Server started...")
    while True:
        client, addr = server.accept()
        print(f"Connect to {addr}")

        client.send(f"Username:".encode('utf-8'))

        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username set to {username}")

        broadcast(f"{username} just joined the chat!".encode('utf-8'))

        client.send("You are now connected!".encode('utf-8'))

        thread = threading.Thread(target=handleConnection, args=(client,))

        thread.start()

if __name__ == "__main__":
    main()
