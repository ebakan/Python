#!/usr/bin/env python
import os,sys,sympy
num=int(sys.argv[1])
mat=[]
s=0
for i in range(1,num+3):
    s+=i**num
    row=[]
    for j in range(num+1,-1,-1):
        row.append(i**j)
    row.append(s)
    mat.append(row)
print '\n'.join([','.join([str(j) for j in i]) for i in mat])
print sympy.Matrix(mat).rref()[0]
