import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
t = raw_input()
rows = []
for i in xrange(h):
    row = raw_input()
    rows.append(row)

# print rows
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

t = t.upper()

for i in xrange(h):
    outrow = ""
    for c in t:
        index = ord(c) - ord("A")
        if index not in xrange((ord("Z") - ord("A")) + 1):
            index = (ord("Z") - ord("A")) + 1
        start = index * l
        outrow = outrow + rows[i][start:start + l]
    print outrow
###
#4
#5
#E
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #
