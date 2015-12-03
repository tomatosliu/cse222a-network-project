import string
import operator
import math
import numpy as np
import pylab as pl
import simplejson as json  
from scapy.all import *

js = json.load(file('data.json'))

dic = {}
for item in js["transfers"]:
	if item["srcAddress"] not in dic:
		dic[item["srcAddress"]] = {}
		dic[item["srcAddress"]]["transfers"] = []
	dic[item["srcAddress"]]["transfers"].append(item)

i = 1
for host in dic:
	name = "host" + str(i) + ".json"
	i = i + 1
	print name
	print dic[host]
	with open(name, 'w') as f:
        	f.write(json.dumps(dic[host]))
