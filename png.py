#!/usr/bin/env python
import sys
class png:
    def __init__(self,i,o):
        self.i=open(i,'rb')
        self.o=open(o,'wb')

    def header(self):
        for i in (137,80,78,71,13,10,26,10):
            self.o.write(chr(i))

    def sizegen(num):
        pairs=[]
        for i in range(1,num+1):
            if not num%i:
                    pairs.append((i,int(num/i)))
        return pairs[math.floor(len(pairs)/2)]

    def rgbencode(inp):
        pixels=[]
        for i in range(math.ceil(len(inp)/3)):
            n=[]
            for k in range(3):
                try:
                    n.append(ord(inp[i*3+k]))
                except IndexError:
                    n.append(0)
            pixels.append(tuple(n))
        return pixels
