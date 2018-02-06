import sys
from socket import *

host = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    #Connect to host:port
    serverSocket.connect((host,int(port)))
    get_request = 'GET /%s HTTP/1.1\r\n\r\nHost:%s:%s' % (filename, host, port)
    serverSocket.send(get_request)
    #get_result = serverSocket.recv(1024)
    #print(get_result)
    result = serverSocket.recv(1024)
    while (len(result) > 0):
        print(result)
        result = serverSocket.recv(1024)
    serverSocket.close()

except IOError:
    serverSocket.close()
    sys.exit()
