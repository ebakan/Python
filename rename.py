#!/usr/bin/python
import sys, os
class Rename:
    def __init__(self):
        self.names=0 #from episode list or not
        self.epsource="episodes" #ep list
        self.offset=0 #offset
        self.lines=1 #line skip from ep list
        self.folder=sys.argv[1]
        self.test=0 #if testing
        self.episodes=self.epsgen(open(self.epsource).readlines(),self.offset,self.lines) if self.names else []
        os.chdir(self.folder)

    def patterngen(self,addnames):
        if addnames: #if reading from list
            return lambda x,y: "[AnCo^2] Durarara!! - %s (1280x720 H264) [%s].mkv" % (x[:2],y)
        else: #if not reading from list, y unused
            return lambda x,y: x[10]+x[12:14]+x[16:-11]+x[-4:]

    def epsgen(self,eps,offset,lines):
        impure=[eps[i] for i in range(offset,len(eps),lines)]
        pure=[i[i.find('"')+1:i.rfind('"')] for i in impure]
        return pure

    def change(self,folder,pattern):
        files=[i for i in os.listdir(folder) if os.path.isfile(i) and i[0]!='.']
        for i in range(len(files)):
            f=files[i]
            try: e=self.episodes[i]
            except IndexError: e=''
            if self.test:
                print os.path.join(folder,pattern(f,e))
            else:
                os.rename(f,os.path.join(folder,pattern(f,e)))

    def rename(self):
        self.change(self.folder,self.patterngen(self.names))

if __name__=='__main__':
    r=Rename()
    r.rename()
