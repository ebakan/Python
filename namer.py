import os
f=open('/users/ebakan/documents/python/names.txt')
l=f.read().split('\n')
f.close()
l=[l[i] for i in range(2,len(l),5)]
n=0
for path, dirs, files in os.walk("/Users/ebakan/Desktop/clannad after story/"):
    for i in files:
        if i[0]!='.':
            os.rename(os.path.join(path,i),
                      os.path.join(path,i[:2]+' '+l[n]+i[-4:]))
            n+=1
