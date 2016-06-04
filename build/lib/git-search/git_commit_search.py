from subprocess import Popen
import os
import sys
try:
    text=sys.argv[1]
except:
    print "please supply a search string"

process=Popen("git_search.sh %s" % ( str(text),), shell=True)
