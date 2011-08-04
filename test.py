#!/usr/bin/env python
def output(x):
    f=[]
    for i in range(2**x):
        n=('{0:0'+str(x)+'d}').format(int(bin(i)[2:])).replace('0','f').replace('1','t')
        f.append('{0}:{1}'.format(i+1,n))
    x=[]
    for i in range(int(len(f)/2)):
        x.append(f[i]+'\t'+f[i+int(len(f)/2)])
    return x

n=open('txt.txt','w')
f=output(6)
for i in f:
    n.write(i+'\n')
n.close()
