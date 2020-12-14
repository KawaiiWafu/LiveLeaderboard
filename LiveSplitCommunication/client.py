import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 16834))

user = input("What's your name? ")
server = input("Server: ")

prev = -1
while True:
    s.send("getsplitindex\r\n".encode())
    new = int(s.recv(4096))
    if prev != new:
        prev = new
        requests.get("/".join((server, user, str(new))))
