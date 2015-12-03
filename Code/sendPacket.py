import string
import operator
import math
import simplejson as json  
from scapy.all import *
import thread
import time

def sending(newpacket):
	print "%s: %s" % ( "threadName", time.ctime(time.time()) )
	newpacket.show()
	send(newpacket)

js = json.load(file('host1.json'))

for packet in js["transfers"]:
	newpacket = IP(dst = packet["dstAddress"], src = packet["srcAddress"], len = 67)/TCP()/"GET / HTTP/1.0\r\n"
	load = "0" * (packet["size"] / 100)
	newpacket = newpacket / load
	try:
		thread.start_new_thread( sending, (newpacket, ) )
	except:
	    print "Error: unable to start thread"
