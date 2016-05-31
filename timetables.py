"""
A function that prints the grade-school multiplication table up to 12x12.

This function accepts n and m and prints up to n times tables.
"""

def tables(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print ("%d x %d = %d\n" % (i, j, i*j))
        print "\n"

tables(14, 14);
