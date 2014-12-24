#!/usr/bin/env python

import sys
from itertools import *

abc=list()
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    trans_id,items = line.split(':',1)
    
    abc=combinations(items,2)
    abc=tuple(set(abc))
    
    #abc=filter(filt,abc) 
    for i in abc:
       	if not (',') in i:
			print "%s\t%s" % (trans_id,1)
	
