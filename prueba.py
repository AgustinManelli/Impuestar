import socket
import threading

host = '127.0.0.1' #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inet=internet, stream=protocolo tcp

server.bind((host, port))
server.listen()
print (f'server running on {host}:{port}')

clients = []
usernames = []

def breoadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_message(client):
    while True:
        try:
            message = client.recv(1024) #bytes
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f'ChatBot: {username} disconnected'.econde('utf-8'))
            client.remove(cleint)
            usenames.remove(username)
            cleint.close()
            break

def receive_connections():
    while True:
        client, address = server.accept()
        client.send('@username'.econde('utf-8'))
        username = cleinte.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print (f'{username} is connected with {str(adress)}')

        message = f'Chatbot: {username} joined the chat'.econde('utf-8')
        broadcast (message, cleint)
        client.send('Connected to server'.econde('utf-8'))

        thread = threading.Thread(target=handle_message(), args=(client,))
        thread.start()

receive_connections()


