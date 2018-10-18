import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'wp.pl'
port = 80
def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False

for x in range(0,5):

    if pscan(x):
        print('Open')
    else:
        print('close')
'''
for x in range(1,10):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')
'''
