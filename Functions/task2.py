"""A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
 """


def make_operation(operator, *args):

    if operator == '+':
        result = 0

        for arg in args:
            if int(arg):
                result += arg

    elif operator == '-':
        result = 0
        for i in range(len(args)-1):
            if int(i):
                result -= args[i+1]
    elif operator == '*':
        result = 1
        for arg in args:
            if int(arg):
                result *= arg
    print(result)


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)