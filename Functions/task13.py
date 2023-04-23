"""Write a function that takes an array of numbers and returns the sum of the numbers.
The numbers can be negative or non-integer. If the array does not contain any numbers then you
should return 0."""


def sum_array(a):
    if not a:
        return 0
    else:
        print(sum(a) )

sum_array([5, 6, 9, 42])
sum_array([1, 2, 3])
sum_array([1.1, 2.2, 3.3, 4.4])