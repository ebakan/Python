#!/usr/bin/env python
import base64, sys, os
string=base64.b64encode(' '.join(sys.argv[1:])).replace('=','')
pb=os.popen('pbcopy','w')
pb.write(string)
pb.close()
sys.stdout.write(string+'\n')
