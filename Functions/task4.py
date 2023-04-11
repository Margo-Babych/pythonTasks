"""Complete the skip_elements function to return every other element from the list,
 this time using the enumerate function to check if an element is on an even position
  or an odd position."""

def skip_elements(elements):
    element = [e for i, e in enumerate(elements) if i % 2 == 0]
    return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']

print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange',
# 'Strawberry', 'Peach']