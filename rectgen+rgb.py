import math
def rectgen(num):
    pairs=[]
    for i in range(1,num+1):
        if not num%i:
            pairs.append((i,int(num/i)))
    return pairs[math.floor(len(pairs)/2)]

def rgbencode(inp):
    pixels=[]
    for i in range(math.ceil(len(inp)/3)):
        n=[]
        for k in range(3):
            try:
                n.append(ord(inp[i*3+k]))
            except IndexError:
                n.append(0)
        pixels.append(tuple(n))
    return pixels

def rgbdecode(inp):
    string=''
    for i in inp:
        for k in i:
            string+=chr(k)
    return string
