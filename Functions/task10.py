"""Write a function that takes in two numbers from the user via input(), call the numbers a and b, and
then returns the value of squared a divided by b, construct a try-except block which raises an exception
 if the two values given by the input function were not numbers, and if value b was zero (cannot divide
  by zero).
Напишіть функцію, яка приймає два числа від користувача за допомогою input(), викликає числа a і b,
 а потім повертає значення квадрата a, поділеного на b, створює блок try-except, який викликає виняток,
  якщо задано два значення функцією введення не були числа, а якщо значення b дорівнювало нулю (не можна
   ділити на нуль).
    """


def squared_divided():

    while True:
        try:
            a = int(input('Enter first number: '))
            b = int(input('Enter second number: '))
            c = (a ** 2) / b
            break
        except ValueError:
            print("No valid integer! Please try again ...")

        except ZeroDivisionError:
            print("Second number can not be zero!")

    print(c)


squared_divided()