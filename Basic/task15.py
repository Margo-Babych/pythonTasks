"""Make a program that has some sentence (a string) on input and returns a dict containing all unique
 words as keys and the number of occurrences as values.

 """
text = str(input("Enter your text: ")).lower()
counts = dict()
words = text.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)