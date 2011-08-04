from matplotlib import pylab
data=open('data.txt').read()
raw_entries=data.split('\n')[:-1]
entries=[i.split(' ') for i in raw_entries]
time=[]
x=[]
v=[]
a=[]
for i in entries:
    time.append(i[0])
    x.append(i[1])
    v.append(i[2])
    a.append(i[3])
pylab.legend(['x','v','a'])
pylab.plot(time,x)
pylab.plot(time,v)
pylab.plot(time,a)
pylab.legend(['x','v','a'])
pylab.show()
