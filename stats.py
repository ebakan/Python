#!/usr/bin/env python
import random, sys
def allSame(b):
    s=b[0]
    for i in b[1:]:
        if i!=s:
            return False
    return True

def shiftBuff(b,v):
    a=b[1:]
    a.append(v)
    return a

def runtime(runs):
    data=[]
    for i in range(1,runs+1):
        buff=[-1,-2,-3,-4,-5];
        count=0
        while not allSame(buff):
            buff=shiftBuff(buff,random.randint(0,1))
            count+=1
        data.append(count)
    print str(runs) + " runs, average: " + str(float(sum(data))/len(data))

if __name__=='__main__':
    if(sys.argc>1):
        runs=int(sys.argv[1]);
    else
        runs=100000
    runtime(runs)
