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
		print '%s\t%s' % (i, 1)
    # increase counters
    #for item in items:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        #item = item.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        #if item.isalnum():
			#print '%s\t%s' % (item, 1)
		
