import socket
import threading

username = input('Enter you username: ')

host = '127.0.0.1' #localhost
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inet=internet, stream=protocolo tcp
client.connect((host, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == '@username':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print ('An error Ocurred')
            client.close

def write_messages():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive_messages())
receive_thread.start()

write_thread = threading.Thread(target=write_messages())
write_thread.start()
