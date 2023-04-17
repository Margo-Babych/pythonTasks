""" example of using  try-except"""

coffee = ["Cafe Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
choice = int(input(" Please, enter number of your choice: "))

try:
    print(coffee[choice])
except:
    print("Invalid number")
finally:
    print("Have a nice day")