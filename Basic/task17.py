"""List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared."""
a_list = []

for i in range(1, 11):
    j = i ** 2
    x = (i, j)
    a_list.append(x)
print(a_list)
