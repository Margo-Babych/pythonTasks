"""Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers"""

import random

i = 0
j = 0
lis1 = []
lis2 = []
while i < 10:
    s = random.randint(1, 10)
    i += 1
    lis1.append(s)
while j < 10:
    s = random.randint(1, 10)
    j += 1
    lis2.append(s)
print(lis1, lis2)
lis3 = set(lis1 + lis2)
print(lis3)