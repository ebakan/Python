#!/usr/bin/env python
import os
n=1
while 1:
    f=os.popen('pbcopy','w')
    f.write(''.join('.' for i in range(n)))
    f.close()
    n+=1
    raw_input()
