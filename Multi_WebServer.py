#import socket module
from socket import *
import sys # In order to terminate the program
import threading

class sub_connection (threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        #Create own TCP for the thread.
        self.connectionSocket = connection
        self.addr = address
        print('Thread connection started for ', self.addr) 

    def run(self):
        response_ok = 'HTTP/1.1 200 OK\r\n\r\n'
        response_notfound = 'HTTP/1.1 404 Not Found\r\n\r\n'
        try:
            message = self.connectionSocket.recv(1024)
            filename = message.split()[1]
            #print(self.addr, ' looking for: ', filename[1:]) 
            f = open(filename[1:])
            outputdata = f.read()
            
            #Send one HTTP header line into socket
            #Fill in start
            self.connectionSocket.send(response_ok)
            #print(self.addr, response_ok)
            #Fill in end
            
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                self.connectionSocket.send(outputdata[i].encode())
            self.connectionSocket.send("\r\n".encode())
            self.connectionSocket.close()
            
        except IOError:
            #Send response message for file not found
            #Fill in start  
            self.connectionSocket.send(response_notfound)
            #Fill in end
            self.connectionSocket.close()
        print('Thread connection finished for ', self.addr) 

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(('', 9876))
    serverSocket.listen(5)
    print('server socket prepared port 9876')
    #Fill in end

    while True:
        #Establish the connection
        print ('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        sub_con = sub_connection(connectionSocket, addr)
        sub_con.start()
        

    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data


main()
