import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of temperatures to analyse
temps = raw_input() # the n temperatures expressed as integers ranging from -273 to 5526
temps_arr = [int(i) for i in temps.split()]
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
closest = [0, sys.maxint]

if len(temps_arr) == 0:
    print 0
else:
    for i,v in enumerate(temps_arr):
        if math.fabs(v) < closest[1]:
            closest = [i, math.fabs(v)]
        else:
            if math.fabs(v) == closest[1]:
                closest = [i, math.fabs(v)] if v > 0 else closest

    print temps_arr[closest[0]]
