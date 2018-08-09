import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inp = input("Input page - ")
x = re.findall("http://(.*)/", inp)
print(str(x))
mysock.connect((str(x[0]), 80))
cmd = str('GET ' + str(inp) + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()