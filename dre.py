#!/usr/bin/env python
def analyze(s):
    v=0
    c=0
    for i in s.lower():
        if i in 'aeiou':
            v+=1
        elif i not in '\n ,.-':
            c+=1
    return (c,v,c+v)
f=open("out.txt")
out=[]
for line in f.readlines():
    consonants=f
    out.append(analyze(line))
print out
f.close()
o=open("data.txt","w")
o.write('\n'.join([', '.join([str(j) for j in i]) for i in out]))

y=[i[0] for i in out]
x=[i[1] for i in out]
print y.index(min(y))
print y.index(max(y))
print x.index(min(x))
print x.index(max(x))

