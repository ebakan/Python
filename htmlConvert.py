def convert(inp):
    encoded=''.join(['&#{0};'.format(ord(i)) for i in inp])
    return '<p>\n{0}\n</p>'.format(encoded.replace('&#10;', '\n</p>\n<p>\n')).replace('<p>\n\n</p>','<br />')

def main():
    file=input("Input File:")
    out=convert(open(file).read())
    for ext in ('.txt', '.html'):
        outfile=open(file+'.converted{0}'.format(ext), 'w').write(out)
        
if __name__=='__main__': main()
