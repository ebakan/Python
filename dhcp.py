#!/usr/bin/python

import os
import random

class Renewer:

    def __init__(self):
	self.prev=[]
	self.connection="en0"

    def getnewaddress(self):
	address=random.randrange(16**12)
	while(self.prev.count(address)>=1):
	    address=random.randrange(16**12)
	self.prev.append(address)
	return address

    def getmacstr(self):
	num=hex(self.getnewaddress())[2:].zfill(12)
	return ':'.join([num[i:i+2] for i in range(0,len(num),2)])

    def enupdown(self):
	os.system("sudo ifconfig %s down && sudo ifconfig %s up" % (self.connection,self.connection))

    def spoofaddress(self, address):
	os.system("sudo ifconfig %s ether %s" % (self.connection,address))

    def spoof(self):
	address=self.getmacstr()
	self.enupdown()
	self.spoofaddress(address)
	print "New Address: %s" % address
	self.enupdown()

if __name__=="__main__":
    r=Renewer()
    r.spoof()
