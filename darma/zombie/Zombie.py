from datetime import datetime


class Zombie:

	def set_output_last_command(self, output):
		if output == "\n" or output == "" or output == " " or output == None:
			output = output
		else:
			self.output_last_command = output

	def update_check_in_time(self):
	        self.last_check_in = datetime.now()

	def __init__(self, uuid, hostname, username, ip, clm):
		self.uuid = uuid
		self.hostname = hostname
		self.username = username
		self.ip = ip
		self.clm = clm
		self.last_check_in = datetime.now()
		self.command_cue = []
		self.output_last_command = ""
