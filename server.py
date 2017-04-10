# import packets and library
from socket import *
import sys
import time
from car import car

#define the function
def server():
    c = car()

    #create a dictionary matching keys and the action
    commands = {'forward':c.forward, 'back':c.back, 'stop':c.stop}

    #start socket connection
    #replace HOST with your own ip
    HOST = 'YOUR_STATIC_IP'
    PORT = 8888
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    #Listener start listening and match the data to the activity of the action
    while True:
        conn, addr = s.accept()
        while True:
            #decode data sent from android app
            command = conn.recv(1024).decode('UTF8')
            command = command.replace('\n','')
            #detect whether there is a legal command received
            if (not command) or (command not in commands):
                break
            #actions
            commands[command]()
        conn.close() 

if __name__ == '__main__':
    server()   

