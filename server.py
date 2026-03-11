import socket

server = socket.socket()
server.bind(("localhost",12345))
server.listen(1)

print("Server waiting...")

conn,addr = server.accept()
print("Connected:",addr)

file = open("data.txt","rb")

data = file.read(1024)
while data:
    conn.send(data)
    data = file.read(1024)

file.close()
conn.close()
server.close()