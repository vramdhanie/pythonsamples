"""
A function to find the largest integer value in an integer array
"""
import sys

def findLargest(numbers):
    large = -sys.maxint - 1
    for i in numbers:
        large = i if large < i else large
    return large

print findLargest([1,2,3,4,5,6,7,8])
print findLargest([8,7,6,5,4,3,2,1])
