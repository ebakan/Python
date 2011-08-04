#!/usr/bin/env python
import string, sys, os
inp=' '.join(sys.argv[1:])
uppercase=False
out=""
for i in inp:
    if i in string.letters:
        out+=i.upper() if uppercase else i.lower()
        uppercase=False if uppercase else True
    else:
        out+=i
os.popen('pbcopy','w').write(out)
print out
