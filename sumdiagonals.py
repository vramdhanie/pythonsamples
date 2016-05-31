n = int(raw_input())
rd = 0
ld = 0
for i in xrange(n):
    row = map(int, raw_input().split())
    rd = rd + row[i]
    ld = ld + row[len(row)- 1 - i]

print "Absolute difference between %d and %d is %d\n" % (rd,ld,abs(rd - ld))
