import string
import operator
import math
import numpy as np
import pylab as pl
import simplejson as json  
from scapy.all import *

js = json.load(file('host1.json'))

for packet in js["transfers"]:
	newpacket = IP(dst = packet["dstAddress"], src = packet["srcAddress"], len = 678)/TCP()/"GET / HTTP/1.0\r\n"
	load = "0" * packet["size"]
	newpacket = newpacket / load
	send(newpacket)
