"""Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters
of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine
 characters

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string) """

import random

str1 = list(input("write the word: "))
i = 0
lis = []
while i < 5:
    random.shuffle(str1)
    list1 = ''.join(str1)
    i += 1
    lis.append(list1)

print(lis)