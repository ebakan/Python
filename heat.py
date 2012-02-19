#!/usr/bin/env python
import md5
import random
while 1:
    randint=random.random()
    randhash=int(md5.md5(str(randint)).hexdigest(),16)
    val=0
    while val!=randhash:
        val+=1
    print "hash found: "+str(randhash)
