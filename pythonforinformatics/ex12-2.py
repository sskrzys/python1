import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inp = input("Input page - ")
#x = re.findall("https://(.*).*/", inp)
x = inp.split("/")
print(str(x))
mysock.connect((str(x[2]), 80))
cmd = str('GET ' + str(inp) + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)
count = 0
letters = 0
numbers = 0
while count < 3001:
    data = mysock.recv(20)
    letters += len(re.findall('[A-z]', str(data)))
    numbers += len(re.findall('[0-9]', str(data)))
    count += len(data)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

print("\nliterek jest %d" % letters)
print("cyferek jest %d" % numbers)

mysock.close()