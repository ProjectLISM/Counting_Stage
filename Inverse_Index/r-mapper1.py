#!/usr/bin/env python

import sys
                                                                                                                              
for line in sys.stdin:

    line = line.rstrip()
    try:
        url,description = line.split('\t')
    except ValueError, e:
        continue
	
    #print description
	
    for word in description.strip().split():
    	word=word.lower()		
	print "%s\t%s\n" %(word,url)
