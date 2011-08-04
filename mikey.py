#!/usr/local/bin/python
import sys, urllib
from BeautifulSoup import BeautifulSoup
class Voter:
    def __init__(self):
        self.url="http://mycollegevideoscholarship.com/"
        self.params=urllib.urlencode({'FormDisplayTime':'http://mycollegevideoscholarship.com/',
                                      'VoteTypeId':'2',
                                      'votePostID':'17',
                                      'votePoint':'1'})
        self.votes=0
        self.handleErrors()
        
    def handleErrors(self):
        try:
            int(sys.argv[1])
        except ValueError:
            sys.argv.append('0')
        except IndexError:
            sys.argv.append('0')
            
    def vote(self):
        urllib.urlopen('http://mycollegevideoscholarship.com/',self.params)
        self.votes+=1

    def votecount(self):
        page=urllib.urlopen('http://mycollegevideoscholarship.com/')
        soup=BeautifulSoup(page)
        raws=soup('div',{'class':'VotingCountDisplay'})
        strings=[str(i) for i in raws]
        return [i[i.find('\t'):i.rfind('\t')].strip() for i in strings] 

    def multivote(self,n,verbose=1):
        def proc():
            self.vote()
            if verbose: print "%d votes" % self.votes if self.votes!=1 else "1 vote"

        if n==-1:
            while 1:
                proc()
        else:
            for i in range(n):
                proc()

    def tally(self):
        print "Alex: %s\nTomomi: %s\nMikey: %s\nMarissa: %s" % tuple(self.votecount())

    def voter(self):
        self.multivote(int(sys.argv[1]))
        self.tally()


if __name__=='__main__':
    voter=Voter()
    voter.voter()
