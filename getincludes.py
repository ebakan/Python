#!/usr/bin/env python
import os,sys,re


if __name__=='__main__':
    if len(sys.argv)>1:
	directory=sys.argv[1]
    else:
	directory=os.getcwd()

    files=os.listdir(directory)
    out=""
    for f in files:
	path=os.path.join(directory,f)
	if os.path.isfile(path) and f[0]!='.':
	    with open(path) as data:
		d=data.read()
		pattern='#include [<|"](.+)[>|"]'
		result=re.findall(pattern,d)
		print f+" : "+' '.join(result)
