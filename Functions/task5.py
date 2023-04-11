"""Pig latin string conversion in python
simple text transformation that modifies each word moving the first character to the end
and appending "oy" to the end."""


def pig_latin(text):
    words = text.split()
    pigged_text = []

    for word in words:
        word = word[1:] + word[0] + 'oy'
        pigged_text.append(word)

    return ' '.join(pigged_text)


print(pig_latin("hello how are you"))
