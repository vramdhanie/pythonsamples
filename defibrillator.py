import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = math.radians(float(raw_input().replace(",", ".")))
lat = math.radians(float(raw_input().replace(",",".")))
n = int(raw_input())

closestDistance = sys.float_info.max
closestName = "UNKNOWN"

for i in xrange(n):
    id, name, address, phone, lond, latd = raw_input().split(";")
    lond = math.radians(float(lond.replace(",", ".")))
    latd = math.radians(float(latd.replace(",", ".")))
    x = (lond - lon) * math.cos((lat + latd)/2)
    y = latd - lat
    d = math.sqrt(x*x + y*y) * 6371
    if d < closestDistance:
        closestDistance = d
        closestName = name

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print closestName
