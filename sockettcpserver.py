import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(("", 9000))
mysocket.listen(1)
connection, fromaddr = mysocket.accept()
while True:
    request = connection.recv(2048)
    print "Got request : " + str(request)
    if "adduser" in request.lower():
        # Code goes here to add a user
        connection.send("New User Added!.\n")
    if "reboot" in request.lower():
        # Code goes here to reboot
        connection.send("System Rebooting now.\n")
