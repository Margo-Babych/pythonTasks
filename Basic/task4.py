"""String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string."""

word = input(" enter your word: ")

if len(word) >= 2:
    print(word[0:2] + word[-2:])
else:
    print("Empty string")