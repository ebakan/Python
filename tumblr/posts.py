#!/usr/bin/env python
from post import post

class regular(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['title']=post.getvalue(self,'regular-title')
        self.attrs['body']=post.getvalue(self,'regular-body')
    
    def htmlbody(self):
        if len(self.attrs['title'])<1:
            return '<div class="body">%s</div>' % self.attrs['body']
        elif len(self.attrs['body'])<1:
            return '<h3 class="title">%s</h3>' % self.attrs['title']
        else:
            return '<h3 class="title">%s</h3>\n<div class="body">%s</div>' % (
                   self.attrs['title'],
                   self.attrs['body'])

class photo(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['caption']=post.getvalue(self,'photo-caption')
        self.attrs['link']=post.getvalue(self,'photo-url')
        self.attrs['height']=elem.getAttribute('height')
        self.attrs['width']=elem.getAttribute('width')

    def htmlbody(self):
        if len(self.attrs['caption'])<1:
            return '<img src="%s"/>' % self.attrs['link']
        else:
            return '<img src="%s"/>\n<div class="caption">%s</div>' % (
                   self.attrs['link'],
                   self.attrs['caption'])

class quote(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['text']=post.getvalue(self,'quote-text')
        self.attrs['source']=post.getvalue(self,'quote-source')

    def htmlbody(self):
        if len(self.attrs['source'])<1:
            return '<h3 class="text">%s</h3>' % self.attrs['text']
        else:
           return '<h3 class="text">%s</h3>\n<div class="source">%s</div>' % (
                   self.attrs['text'],
                   self.attrs['source'])

class link(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['text']=post.getvalue(self,'link-text')
        self.attrs['link']=post.getvalue(self,'link-url')

    def htmlbody(self):
        if len(self.attrs['text'])<1:
            return '<h3 class="title"><a href="%s">%s</a></h3>' % (
                   self.attrs['link'],
                   self.attrs['link'])
        else:
           return '<h3 class="title"><a href="%s">%s</a></h3>' % (
                   self.attrs['link'],
                   self.attrs['text'])


class conversation(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['title']=post.getvalue(self,'conversation-title')
        self.attrs['text']=post.getvalue(self,'conversation-text')
        self.attrs['conversation']=post.getvalue(self,'conversation')

    def htmlbody(self):
        if len(self.attrs['title'])<1:
            return '<div class="text">%s</div>' % self.attrs['text']
        else:
            return '<h3 class="title">%s</h3>\n<div class="text">%s</div>' % (
                   self.attrs['title'],
                   self.attrs['text'])


class video(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['caption']=post.getvalue(self,'video-caption')
        self.attrs['source']=post.getvalue(self,'video-source')
        self.attrs['player']=post.getvalue(self,'video-player')

    def htmlbody(self):
        if len(self.attrs['caption'])<1:
            return self.attrs['player']
        else:
            return '%s\n<div class="caption>%s</div>' % (
                   self.attrs['player'],
                   self.attrs['caption'])


class audio(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['caption']=post.getvalue(self,'audio-caption')
        self.attrs['player']=post.getvalue(self,'audio-player')
        self.attrs['download']=post.getvalue(self,'download-url')

    def htmlbody(self):
        if len(self.attrs['caption'])<1:
            return '%s\n<a href="%s">Download</a>' % (
                   self.attrs['player'],
                   self.attrs['download'])
        else:
            return '%s\n<a href="%s">Download</a>\n<div class="caption">%s</div>' % (
                   self.attrs['player'],
                   self.attrs['download'],
                   self.attrs['caption'])

class answer(post):
    def __init__(self,elem):
        post.__init__(self,elem)
        self.attrs['question']=post.getvalue(self,'question')
        self.attrs['answer']=post.getvalue(self,'answer')

    def htmlbody(self):
        return '<h3 class="question">%s</h3>\n<div class="question">%s</div>' % (
               self.attrs['question'],
               self.attrs['answer'])
