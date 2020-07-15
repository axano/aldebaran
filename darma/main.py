import daemon
import threading
import listener
import command
import config


# To deamonize or not to deamonize (see config.py)
if config.daemonize:
	out = open(config.log_file, 'w+')
	with daemon.DaemonContext(stdout=out,stderr=out):
		tasks = [command.start, listener.start]
		for task in tasks:
			t = threading.Thread(target=task)
			t.start()

else:
	tasks = [command.start, listener.start]
	for task in tasks:
		t = threading.Thread(target=task)
		t.start()
