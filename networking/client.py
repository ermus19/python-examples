import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

sk.connect((host, port))

msg = sk.recv(2048)

sk.close()

print (msg.decode('ascii'))