import string
import operator
import math
import json  
from scapy.all import *

js = json.load(file('data.json'))
ip = json.load(file('ip.json'))

dic = {}
for item in js["transfers"]:
	item["srcAddress"] = ip[item["srcAddress"]]
	item["dstAddress"] = ip[item["dstAddress"]]
	
	if item["srcAddress"] not in dic:
		dic[item["srcAddress"]] = {}
		dic[item["srcAddress"]]["transfers"] = []
	dic[item["srcAddress"]]["transfers"].append(item)

i = 1
for host in dic:
	name = host + ".json"
	i = i + 1
	print name
	with open(name, 'w') as f:
        	f.write(json.dumps(dic[host]))
