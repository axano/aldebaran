# aldebaran

Python3 C2 server and agent payload.

uses HTTP protocol with checkin. Works in env with powershell constrained language mode.

Agent code can be delivered as in memory only or as is e.g in a hta file.

darma is the server side code in python3

darpa is the agent side code in powershell

# Installation

install requirements with pip3

you will have to create valid https certs.
Self signed certs wont work with powershell. will lose constrainedlanguagemode support to ignore ssl errors so use letsencrypt

use ```certbot certonly --manual -d 220.ip-54-37-16.eu -d 220.ip-54-37-16.eu --register-unsafely-without-email ```
and copy certs in same directory as "darma/listener.py"

you will have to create valid https certs.
Change payload to point to your server url


Change bcrpyt hash in "darma/command.py" with

```
#Python3
# To generate hash
# Mind the '\n'
password = b"super secret password\n"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
```

To start server:

```
python3 darma/main.py
```

run agent on victim

connect to server with netcat on port 51251

```
nc ip_of_server 51251
```

enter password and menu will pop up


## TODO
### Persistence
