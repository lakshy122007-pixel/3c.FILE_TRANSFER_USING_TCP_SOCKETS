# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS
## AIM
To write a python program for creating File Transfer using TCP Sockets Links
## ALGORITHM:
1. Start the program.
2. Import the socket module in both server and client programs.
3. Create a socket using socket.socket() on the server side.
4. Bind the server socket to localhost and port 12345 using bind().
5. Make the server wait for client connection using listen() and accept().
6. Open the file data.txt in read binary mode (rb) on the server.
7. Read the file in chunks using read(1024) and send the data to the client using send().
8. On the client side, create a socket and connect to the server using connect().
9. Receive the file data using recv(1024) and write it into received.txt in write binary mode (wb).
10. Close the file and socket connections on both client and server, then stop the program.
## PROGRAM
```
server:
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


client:
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
```
## OUPUT
server:
![alt text](<3.c serv.png>)

client:
![alt text](<3.c client.png>)
## RESULT
Thus, the python program for creating File Transfer using TCP Sockets Links was 
successfully created and executed.
