import sys
import math

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            swap(a, i, j)
    swap(a, i + 1, r)
    return i + 1

def sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        sort(a, p, q - 1)
        sort(a, q + 1, r)

horses = []
n = int(input())
for i in range(n):
    pi = int(input())
    horses.append(pi)
closest = float("inf")
sort(horses, 0, n - 1)
for i in range(n-1):
    if math.fabs(horses[i] - horses[i+1]) < closest:
        closest = math.fabs(horses[i] - horses[i+1])

print(int(closest))
