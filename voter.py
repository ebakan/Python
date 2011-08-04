#!/usr/bin/env python
import sys,urllib,urllib2
from BeautifulSoup import BeautifulSoup
class Voter:
    def __init__(self):
        self.url="https://mail.bcp.org/exchweb/bin/auth/owaauth.dll"
        self.params=urllib.urlencode({'destination':'https://mail.bcp.org/exchange/',
                                      'flags':'0',
                                      'username':'eric.bakan12',
                                      'password':'ZXJpY2Jha2Fu',
                                      'SubmitCreds':'Log On',
                                      'trusted':'0'})
        print self.params
        self.votes=0
        self.handleErrors()

    def handleErrors(self):
        try:
            int(sys.argv[1])
        except ValueError:
            sys.argv.append('0')
        except IndexError:
            sys.argv.append('0')
            
    def count(self,page):
        soup=BeautifulSoup(page)
        (x,)=soup('td',{'class':"SurveyAnswer sAnswerChoiceVotes sAnswerChoiceVotes3"})
        x=str(x)
        return int(x[64:x.rfind('<')].replace(',',''))        

    def vote(self):
        self.votes+=1
        return urllib2.urlopen(self.url,self.params)

    def main(self):
        print urllib2.urlopen(self.url,self.params).read()
#page=self.vote()
#print self.votes
#print self.count(page)

if __name__=='__main__':
    v=Voter()
#while 1:
    v.main()
