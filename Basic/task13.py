"""Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration"""

lis1 = list(range(1, 101))

i = 1
lis2 = []
while i in lis1:

    if i % 7 == 0 and i % 5 != 0:
        lis2.append(i)
    i += 1
print(lis2)
