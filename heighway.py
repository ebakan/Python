#!/usr/bin/env python
class heighway:
    def __init__(self,d,steps):
        self.position=[0,0]
        self.directions=['u','r','d','l']
        self.direction=0
        self.d=d
        self.steps=steps
        self.count=0
        self.depth=0
        self.checker('Fa')
        
    def checker(self,text):
        for i in text:
            if self.count<self.steps and self.depth<self.d:
                if i=='F':
                    if self.direction==0:
                        self.position[1]+=1
                    elif self.direction==1:
                        self.position[0]+=1
                    elif self.direction==2:
                        self.position[1]-=1
                    elif self.direction==3:
                        self.position[0]-=1
                    self.count+=1
                elif i=='R':
                    self.direction=(self.direction+1)%4
                elif i=='L':
                    self.direction=(self.direction+4-1)%4
                elif i=='a':
                    self.depth+=1
                    self.checker('aRbFR')
                    self.depth-=1
                elif i=='b':
                    self.depth+=1
                    self.checker('LFaLb')
                    self.depth-=1

if __name__=='__main__':
    #h=heighway(10,500)
    h=heighway(50,10**12)
    print h.position
