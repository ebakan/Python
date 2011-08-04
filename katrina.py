import os
while 1:
    x='_'.join(i.strip() for i in raw_input())
    outf = os.popen("pbcopy", "w")
    outf.write(x)
    outf.close()
