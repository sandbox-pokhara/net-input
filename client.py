import socket

host, port = "127.0.0.1", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b"mouse,move,100,100", (host, port))
sock.sendto(b"keyboard,write,Hello World", (host, port))
