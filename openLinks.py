#!/usr/bin/env python
import sys, webbrowser
fileName=sys.argv[1]
f=open(fileName)
for i in f.readlines():
    webbrowser.open(i)
f.close()
