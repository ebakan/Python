#!/usr/bin/python
import os
def sort(x):
    names=[' - '.join((i[1],i[4])) for i in [i.split('\t') for i in x.split('\n')[:-2]]]
    for i in range(len(names)):
        names[i]=str(i+1)+' '+names[i]
    return '\n'.join(names)
x=sort(open('.playlist').read())
print x
os.popen('pbcopy','w').write(x)
