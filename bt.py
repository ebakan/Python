#!/usr/bin/python
import os
root="/Users/ebakan/Desktop/"
folderkey="next"
folder=os.path.join(root,[i for i in os.listdir(root) if i[:len(folderkey)]==folderkey][0])
s=0
for i in os.listdir(folder):
    if i[0]!='.':
        s+=float(i[i.rfind(' ')+1:-8])
os.rename(folder,'%s %.2f/' % (root+folderkey,s))
print "%s %.2f" % (folderkey, s)
