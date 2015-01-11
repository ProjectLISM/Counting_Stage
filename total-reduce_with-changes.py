"""
This code converts the transactions into co-occurences
"""

import sys

def occurence(current_id,current_count,trans_id,line):
    """
    Args:
        current_id (string): 
        current_count (int): 
        trans_id (int): 
        line (string): To read from file
    """
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    trans_id,count = line.split('\t',1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_id == trans_id:
        current_count += 1
    else:
        if current_id:
            # write result to STDOUT
            print '%s\t%s' % (current_id, current_count)
        current_count = count
        current_id = trans_id

# do not forget to output the last word if needed!
if current_id == trans_id:
    print '%s\t%s' % (current_id, current_count)


current_id=None
current_count = 0
trans_id=None

# input comes from STDIN
for line in sys.stdin:
    occurence(current_id,current_count,trans_id,line)
