import socket

target = '127.0.0.1'
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(str.encode("Text"),(target, port))

data, addr = client.recvfrom(4096)

print(data)