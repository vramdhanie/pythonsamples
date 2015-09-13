import sys
import math

def getBits(c):
    return bin(ord(c))[2:].zfill(7)

def firstZero(s):
    if len(s) > 0:
        if(s[0:1] == "1"):
            tail = " " + firstOne(s[1:])
        else:
            tail = moreZeros(s[1:])
    else:
        tail = ""
    return "00 0" + tail

def firstOne(s):
    if len(s) > 0:
        if s[0:1] == "0":
            tail = " " + firstZero(s[1:])
        else:
            tail = moreOnes(s[1:])
    else:
        tail = ""

    return "0 0" + tail

def moreZeros(s):
    if len(s) > 0:
        if(s[0:1] == "1"):
            tail = " " + firstOne(s[1:])
        else:
            tail = moreZeros(s[1:])
    else:
        tail = ""
    return "0" + tail

def moreOnes(s):
    if len(s) > 0:
        if s[0:1] == "0":
            tail = " " + firstZero(s[1:])
        else:
            tail = moreOnes(s[1:])
    else:
        tail = ""
    return "0" + tail;

message = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

encoded = "".join(map(lambda x:getBits(x), message))

print encoded

if encoded[0:1] == "0":
    print firstZero(encoded[1:])
else:
    print firstOne(encoded[1:])
