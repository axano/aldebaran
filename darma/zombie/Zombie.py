import secrets
from datetime import datetime



class Zombie:
	def __init__(self):
		self.id = secrets.token_urlsafe(32)
		self.public_ip = ""
		self.hostname = ""
		self.last_check_in = datetime.now()
		self.command_cue = []
