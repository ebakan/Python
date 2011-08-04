#!/usr/bin/env python
import urllib2
for i in range(1,1571):
    url=urllib2.urlopen('http://questionablecontent.net/comics/%d.png' % i)
    pic=open('%d.png' % i,'w')
    pic.write(url.read())
    url.close()
    pic.close()
    print i
    
