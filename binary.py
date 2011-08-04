#!/usr/bin/env python
import os, sys
def encode(text):
    return ' '.join(bin(ord(i))[2:].zfill(8) for i in text)

def decode(text):
    text=text.replace('\n','00001010').replace(' ','')
    text=[text[i-8:i] for i in range(8,len(text),8)]
    return ''.join([chr(int(i,2)) for i in text])

if __name__=='__main__':
    func=encode if sys.argv[1]=='-e' else decode
    arg=2 if len(sys.argv)>2 else 1
    if os.path.isfile(sys.argv[arg]):
        print func(sys.argv[arg].read())
    else:
        print func(' '.join(sys.argv[arg:]))
