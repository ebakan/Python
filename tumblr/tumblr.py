#!/usr/bin/env python
import base64, urllib, xml.dom.minidom
from post import post
from posts import *

class tumblr:
    def __init__(self):
        self.address="http://www.tumblr.com/api/dashboard"
        self.params={'email':base64.b64decode('YmFrYW5hdG9yekBnbWFpbC5jb20='),
                     'password':base64.b64decode('a2F0cmluYWlzY29vbA=='),
                     'start':0,
                     'num':10,
                     'type':''}
        self.mapping={'regular':regular,
                      'photo':photo,
                      'quote':quote,
                      'link':link,
                      'conversation':conversation,
                      'video':video,
                      'audio':audio,
                      'answer':answer}
        self.doctype='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">'
        self.header='<title>eTumblr</title>\n<link rel="icon" href="http://assets.tumblr.com/images/favicon.gif"/>'
        self.doc=self.getdoc()
        self.posts=[self.classify(i) for i in self.getposts()]
        self.outpath='tumblr.html'
        self.writeout(self.outpath)

    def getdoc(self):
        params=urllib.urlencode(self.params)
        page=urllib.urlopen(self.address,params)
        return xml.dom.minidom.parse(page)

    def getposts(self):
        return self.doc.getElementsByTagName("post")
   
    def posttype(self,elem):
        return elem.getAttribute('type')

    def classify(self,elem):
        return self.mapping.get(self.posttype(elem),post)(elem)

    def postshtml(self):
        return '<div class="posts">\n\t\t\t%s\n\t\t</div>' %(
               '\n\t\t\t'.join([i.html().replace('\n','\n\t\t\t') for i in self.posts]))

    def genhtml(self):
        return '%s\n<html>\n\t<head>\n\t\t%s\n\t</head>\n\t<body>\n\t\t%s\n\t</body>\n</html>' % (
               self.doctype,
               self.header.replace('\n','\n\t\t'),
               self.postshtml())


    def writeout(self,outpath):
        f=open(outpath,'w')
        f.write(self.genhtml().encode('utf-16'))
        f.close()

if __name__=='__main__':
    t=tumblr()
