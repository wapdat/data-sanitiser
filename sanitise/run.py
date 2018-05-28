import sys
import re
import time
import sanitise 

if len(sys.argv) < 2:
    print('Exit code 10: Please enter a string to regexReplace and optionally -v for verbose')
    sys.exit(10)
    
str = sys.argv[1]
original = str
debug = False
list = ''

if (len(sys.argv) == 3):
    if (sys.argv[2] == '-v'):
        debug = True


milli_sec_start = int(round(time.time() * 1000))
if (debug) : print('%-20s "%s"' % ('Unsanitised', str))

str = sanitise.tokenise(str)
str = sanitise.replacePPI(str)

if (debug): print('%-20s "%s"' % ('Test list: ', list))
if (debug) : print (original)

print (str)

if (debug):
    milli_sec_end = int(round(time.time() * 1000))
    print('%-20s "%s"' % ('Processing time milli seconds: ', milli_sec_end - milli_sec_start))


