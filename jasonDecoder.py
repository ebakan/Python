#!/usr/bin/env python
inp=raw_input().replace("&#", '').replace(';', ' ')
inp=inp.split(' ')
inp=map(lambda x: hex(int(x))[2:], inp[:-1])
out=[]
for i in inp:
    out.append(i[:2])
    out.append(i[2:])
out=map(lambda x: chr(int(x,16)), out)
print ''.join(out)
