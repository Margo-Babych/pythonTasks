"""The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers """

import random

i = 0
lis = []
while i < 10:
    s = random.randint(1, 100)
    i += 1
    lis.append(s)
print(lis)
lis.sort()
print(lis[-1])