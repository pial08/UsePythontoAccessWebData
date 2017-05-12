import socket
import urllib


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))

mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data
mysock.close()

"""

fhand = urllib.urlopen('http://data.pr4e.org/intro-short.txt')

for line in fhand:
    print line.strip()
"""