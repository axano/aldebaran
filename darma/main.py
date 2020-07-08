import daemon
import threading
import listener
import command

#"""
out = open('/var/log/aldebaran.log', 'w+')
with daemon.DaemonContext(stdout=out,stderr=out):
	tasks = [command.start, listener.start]
	for task in tasks:
		t = threading.Thread(target=task)
		t.start()

"""
tasks = [command.start, listener.start]
for task in tasks:
	t = threading.Thread(target=task)
	t.start()
"""
