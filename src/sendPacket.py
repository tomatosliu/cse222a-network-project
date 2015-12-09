import string
import operator
import math
import json  
from scapy.all import *
import thread
import time
import netifaces as ni

ip = ni.ifaddresses(ni.interfaces()[1])[2][0]['addr']

def sending(newpacket):
	print "%s: %s" % ( "threadName", time.ctime(time.time()) )
	#newpacket.show()
	send(newpacket)

js = json.load(file(ip + '.json'))

for packet in js["transfers"]:
	newpacket = IP(dst = packet["dstAddress"], src = packet["srcAddress"], len = 67)/TCP()/"GET / HTTP/1.0\r\n"
	load = "0" * (packet["size"] / 100000)
	newpacket = newpacket / load
	try:
		thread.start_new_thread( sending, (newpacket, ) )
	except:
	    print "Error: unable to start thread"

while 1:
	pass
