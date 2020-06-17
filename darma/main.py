import daemon
import threading
import command
import listener


with daemon.DaemonContext():
	tasks = [command.start, listener.start]
	for task in tasks:
		t = threading.Thread(target=task)
		t.start()
