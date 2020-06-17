import daemon
import threading
import listener
import command

"""
with daemon.DaemonContext():
	tasks = [command.start, listener.start]
	for task in tasks:
		t = threading.Thread(target=task)
		t.start()
"""
tasks = [command.start, listener.start]
for task in tasks:
	t = threading.Thread(target=task)
	t.start()
