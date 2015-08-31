"""
A function that sums up integers from a text file, one int per line.

The text file is first generated using a random integer.
"""

import numpy as np

def makeNumbers(N, M):
    numbers = np.random.randint(M, size=N)
    np.savetxt("numbers.txt", numbers, delimiter=",", fmt="%d")

def sumints():
    f = open('numbers.txt', 'rU')
    sum = 0
    for line in f:   ## iterates over the lines of the file
        sum+=int(line)
    f.close()
    return sum

makeNumbers(50, 200)
print (("The sum of the integers in the file is %d")%(sumints()))
