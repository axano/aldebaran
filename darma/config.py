# General 
domain = "dummy.domain.com"
installation_path = "/opt/aldebaran/"
daemonize = False

# Command server side

## bcrypt password hash
## Example hash creation (add \n to end of string)
## password = b"super secret password\n"
## Hash a password for the first time, with a randomly-generated salt
## hashed = bcrypt.hashpw(password, bcrypt.gensalt())
## print(hashed)
bcrypt_password_hash = b'$2b$12$5f2z5D3nmeGV0bVOKmJlXuM0ncQXHu9IokJWe/XZZEVc4cxUV3sZS'

server_bind_ip = "0.0.0.0"
server_bind_port = 51251
log_file = '/var/log/aldebaran.log'

# Webserver
## Use letsencrypt to generate legitimate cert. PS will flip otherwise.
## Copy certs in same directory as listener.py
## certbot certonly --manual -d dummy.domain.com  --register-unsafely-without-email
## lifetime is forced to 90 days
key_file = "/opt/aldebaran/darma/certificates/key.pem"
cert_file = "/opt/aldebaran/darma/certificates/cert.pem"
