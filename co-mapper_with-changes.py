#!/usr/bin/env python
"""
This code converts customer transactions to co-occurences
"""

import sys
from itertools import *

def occurence(abc,line):
    """
    This function validates transaction IDs and creates co-occurence information
    Args:
        abc (list): list to store products
        line (string): to read from file
    """
    line = line.strip()
    trans_id,items = line.split(':',1)
    abc = combinations(items,2)
    abc = tuple(set(abc))
    for i in abc:
        if (',') not in i:
            print '%s\t%s' % (i, 1)

"""
Input comes from STDIN (Standard Input)
"""
abc=list()
for line in sys.stdin:
    occurence(abc,line)
