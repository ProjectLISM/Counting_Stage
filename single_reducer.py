#!/usr/bin/env python

import sys

current_item = None
current_count = 0
item = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    item, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_item == item:
        current_count += count
    else:
        if current_item:
            # write result to STDOUT
            print '%s\t%s' % (current_item, current_count)
        current_count = count
        current_item = item

# do not forget to output the last word if needed!
if current_item == item:
    print '%s\t%s' % (current_item, current_count)
