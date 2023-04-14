"""The format_address function separates out parts of the address string into new strings:
house_number and street_name, and returns: "house number X on street named Y".

The format of the input string is: numeric house number, followed by the street name which may contain
 numbers, but never by themselves, and could be several words long. For example, "123 Main Street",
 "1001 1st Ave", or "55 North Center Drive"."""


def format_address(address_string):
    num, st = address_string.split(' ', 1)
    return f"house number {num} on street named {st}"


print(format_address("13 Main Street"))
