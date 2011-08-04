class hbcli:
    
    #Import global modules and set global variables
    def __init__(self):
        #import os and make global
        import os
        global os
        #set global variables
        self.inpath="/Users/ebakan/Desktop/in/"
        self.outpath="/Users/ebakan/Desktop/out/"
        self.outext=".mp4"
        self.options="-X 480 -Y 360"
        #forbidden characters and their replacements
        self.forbidden={'!':'\\e'}
 
    #replace forbidden characters
    def placeholder(self,path):
        for path, dirs, files in os.walk(path):
            for i in filter(lambda x: x[0]!='.',files):
                name=i
                for j,k in self.forbidden.items():
                    name=name.replace(j,k)
                os.rename(path+i, path+name)

    #get list of files            
    def getfiles(self,path):          
        for path, dirs, files in os.walk(path):
            return map(lambda x: os.path.join(path,x), filter(lambda x: x[0]!='.', files))
        
    #generate terminal command    
    def gencmd(self,data):
        def foo(x):
            name=os.path.split(x)[1]
            basename=os.path.splitext(name)[0]
            return 'HandBrakeCLI -i "%s" -o "%s" %s' % (x, os.path.join(self.outpath, basename+self.outext),self.options)
        return '; '.join(map(foo,data))

    #placeholder for the placeholder method
    def pre(self):
        self.placeholder(self.inpath)
    #pastes the valid command to the pasteboard
    def main(self):
        print(self.gencmd(self.getfiles(self.inpath)))
        
    #remove placeholder characters   
    def post(self):
        for dirname in (self.inpath, self.outpath):
            for path, dirs, files in os.walk(dirname):
                for i in filter(lambda x: x[0]!='.',files):
                        root, ext = os.path.splitext(i)
                        for j,k in self.forbidden.items():
                            root=root.replace(k,j)
                        os.rename(os.path.join(path,i), os.path.join(path, root+ext))

if __name__=='__main__':
    hb=hbcli()
    hb.main()
