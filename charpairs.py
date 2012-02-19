#!/usr/bin/env python
import sys
s=sys.stdin.read().strip()
d=dict()
for i in range(len(s)-1):
    chars=s[i]+s[i+1]
    try:
        d[chars]+=1
    except KeyError:
        d[chars]=1
for i in d.keys():
    print i+": "+str(d[i])
