#!/usr/bin/env python
import sys, os, base64, urllib, xml.dom.minidom

class imgur:
    def __init__(self):
        self.params={'key':'ee284ca35373119234138e5c85b590de'}
        self.url='http://api.imgur.com/2/upload'

    def b64(self,file):
        return base64.b64encode(open(file,'rb').read())

    def process(self,data):
        self.params['image']=self.b64(data)

    def sideload(self,url):
        self.params['image']=url

    def parseresponse(self,response):
        return xml.dom.minidom.parse(response)
    
    def pathfinder(self,xml,path):
        node=xml
        for i in path.split('/'):
            node=node.getElementsByTagName(i)[0]
        return node.firstChild.nodeValue

    def link(self):
        return self.pathfinder(self.response,'upload/links/original').replace("http://","http://i.")

    def post(self,imgpath):
        if os.path.isfile(imgpath):
            self.process(imgpath)
        else:
            self.params['image']=imgpath
        self.response=self.parseresponse(urllib.urlopen(self.url,urllib.urlencode(self.params)))
        return self.link()

    def ding(self):
	os.system("afplay /System/Library/Sounds/Glass.aiff");
    
if __name__=='__main__':
    imgur=imgur()
    links=[]
    if os.path.isdir(sys.argv[1]):
        sys.argv+=[os.path.join(sys.argv[1],i) for i in os.listdir(sys.argv[1]) if i[0]!='.']
        del sys.argv[1]
    for i in sys.argv[1:]:
        sys.stdout.write(i+': ')
        sys.stdout.flush()
        link=imgur.post(i)
        sys.stdout.write(link+'\n')
        sys.stdout.flush()
        links.append(link)
    os.popen('pbcopy','w').write('\n'.join(links))
    imgur.ding();
