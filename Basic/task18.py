"""Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,"""

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_days = []
days_of_week = []
for index in range(len(week)):
    week_days.append({index + 1: week[index]})
    days_of_week.append({week[index]: index + 1})

print(week_days)
print(days_of_week)
