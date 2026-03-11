import socket

client = socket.socket()
client.connect(("localhost",12345))

file = open("received.txt","wb")

data = client.recv(1024)
while data:
    file.write(data)
    data = client.recv(1024)

file.close()
client.close()

print("File received successfully")