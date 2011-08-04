import urllib
def prettyprint(x):
    levels=0
    out=''
    items=[i+'>' for i in x.split('>')][:-1]
    for i in range(len(items)):
        if(items[i][:2]=='</'): #closing tag
            levels-=1
            out+=items[i]
        elif(items[i][-2:]=='/>'): #autoclosing tag
            out+=items[i]
        else: #normal tag
            out+=items[i]
            levels+=1
        out+=str(levels)+'\n'+'\t'*levels
    return out

if(__name__=='__main__'):
    x=urllib.urlopen('http://google.com/complete/search?output=toolbar&q=microsoft').read()
    print x
    print prettyprint(x)
    
