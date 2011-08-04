#!/usr/bin/env python
import time

class post:
    def __init__(self,elem):
        self.elem=elem
        self.attrlist=['reblogged-from-name','reblogged-from-url',
                       'reblogged-root-name','reblogged-root-url',
                       'tumblelog','type','unix-timestamp',
                       'note-count','url-with-slug']
        self.attrs=self.getattrs()
        self.tags=self.getvalues('tag')

    def getattrs(self):
        attrs={}
        for attr in self.attrlist:
            attrs[attr]=self.elem.getAttribute(attr).encode()
        self.attrfilter(attrs)
        attrs['timestamp']=time.localtime(int(attrs['unix-timestamp']))
        del attrs['unix-timestamp']
        attrs['time']=time.asctime(attrs['timestamp'])
        return attrs

    def attrfilter(self,attrs):
        if attrs[self.attrlist[0]]=='':
            for i in range(4):
                del attrs[self.attrlist[i]]
            attrs['reblogged']=-1
        elif attrs[self.attrlist[0]]==attrs[self.attrlist[2]]:
            for i in range(2):
                del attrs[self.attrlist[i+2]]
            attrs['reblogged']=0
        else:
            attrs['reblogged']=1

    def getvalue(self,tag):
        try:
            return self.elem.getElementsByTagName(tag)[0].firstChild.nodeValue
        except IndexError:
            return ''
    
    def getvalues(self,tag):
        try:
            return [i.firstChild.nodeValue for i in self.elem.getElementsByTagName(tag)]
        except IndexError:
            return ''

    def htmlheader(self):
        if self.attrs['reblogged']>0:
            return '<h1 class="header">\n\t<a href="%s">%s</a> reblogged <a href="%s">%s</a>: (<a href="%s">%s</a>)\n</h1>' % (
                    self.attrs['url-with-slug'],
                    self.attrs['tumblelog'],
                    self.attrs['reblogged-from-url'],
                    self.attrs['reblogged-from-name'],
                    self.attrs['reblogged-root-url'],
                    self.attrs['reblogged-root-name'])

        elif self.attrs['reblogged']==0:
            return '<h1 class="header">\n\t<a href="%s">%s</a> reblogged <a href="%s">%s</a>:\n</h1>' % (
                    self.attrs['url-with-slug'],
                    self.attrs['tumblelog'],
                    self.attrs['reblogged-from-url'],
                    self.attrs['reblogged-from-name'])
        else:
            return '<h1 class="header">\n\t<a href="%s">%s</a>:\n</h1>' % (
                   self.attrs['url-with-slug'],
                   self.attrs['tumblelog'])

    def htmlinfo(self):
        return '<p class="info">%s @ %s</p>' % (
               self.attrs['type'],
               self.attrs['time'])

    def htmlbody(self):
        return ''

    def html(self):
        return '<div class="%s">\n\t%s\n\t%s\n\t%s\n</div>' % (
               self.attrs['type'],
               self.htmlheader().replace('\n','\n\t'),
               self.htmlinfo(),
               self.htmlbody().replace('><','>\n\t<').replace('\n','\n\t'))

