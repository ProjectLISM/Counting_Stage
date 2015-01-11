#!/usr/bin/env python
"""
This code reads the intermediate file of co-occurences and takes the count of each different co-occurence
"""

def occurence(current_item,current_count,item,line):
    """
    This function reads the file and counts all the co-occurences of each pair

    Args:
        current_item (string): Current Itemset
        current_count (int): Current Count
        item (string): Item name read from file
        line (string): to read from file
    Raises:
        ValueError: If 'count' not equal to '(int)count'
    """
    line = line.strip()
    item,count = line.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_item == item:
        current_count += count
    else:
        if current_item:
            print '%s\t%s' % (current_item, current_count)
        current_count = count
        current_item = item
    if current_item == item:
        print '%s\t%s' % (current_item, current_count)

import sys

current_item = None
current_count = 0
item = None

"""
Input comes from STDIN
"""
for line in sys.stdin:
    occurence(current_item,current_count,item,line)
