"""
Write a function called oops that explicitly raises an IndexError exception when called. Then write another
 function that calls oops inside a try/except state­ment to catch the error. What happens if you change
 oops to raise KeyError instead of IndexError?
Завдання 1

Напишіть функцію під назвою oops, яка під час виклику явно викликає виключення IndexError. Потім напишіть іншу
 функцію,
 яка викликає oops у операторі try/except, щоб виявити помилку. Що станеться, якщо ви зміните oops на виклик
 KeyError замість IndexError?
 """


def oops():
    raise IndexError


def anotherfunc():
    try:
        oops()
    except:
        print("Error caught")


def oops2():
    raise KeyError

