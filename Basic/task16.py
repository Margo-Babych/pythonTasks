"""Compute the total price of the stock where the total price is the sum of the price
 of an item multiplied by the quantity of this exact item."""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = 0
for key in prices:
    total_price += prices[key] * stock[key]
print(total_price)
