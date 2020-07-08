# aldebaran

Python3 C2 server and agent payload.

uses HTTP protocol with checkin. Works in env with powershell constrained language mode.

Agent code can be delivered as in memory only or as is e.g in a hta file.

DARMA is the server side code in python3
DARPA is the agent side code in powershell



you will have to create valid https certs.

use ```certbot certonly --manual -d 220.ip-54-37-16.eu -d 220.ip-54-37-16.eu --register-unsafely-without-email ```

## TODO
### Persistence
