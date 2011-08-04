#!/usr/bin/env python
import urllib.request

def genterm(inp):
    def foo(x):
        if x.isalpha():
            return x
        else:
            return '%{0}'.format(hex(ord(x))[2:])
    return ''.join(map(foo,inp))

def genresults(inp):
    page=urllib.request.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+inp)
    query=eval(page.read().decode().replace('null','None'))
    page.close()
    return int(list(list(query.values())[0].values())[0]['estimatedResultCount'])
   
def main():
    terms={}
    
    counter=3
    for i in range(1,counter+1):
        for k in range(1,counter+1):
            terms['f'*i+'u'*k]=None
            
    for i in terms.keys(): terms[i]=genresults(genterm(i))
    return sorter(terms)

def sorter(dictionary):
    keys=list(dictionary.keys())
    keys.sort()
    vals=[dictionary[i] for i in keys]
    return dict(zip(keys,vals))

def output(terms):
    f=open('fu.csv','w')
    for i in terms:
        f.write('{0},{1},{2}\n'.format(i[0].count('f'),i[0].count('u'),i[1]))

if __name__=='__main__':
    output(main())
