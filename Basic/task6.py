"""The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
 and then responds with a message accordingly.

 """

answer = int(input(" 2**3 = ?       Your answer is: "))
if answer == 8:
    print("Yes, that\'s right!!!" + "\U0001F604")
else:
    print("Oh, no. " + "\N{flushed face}")