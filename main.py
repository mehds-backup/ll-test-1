# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fizzbuzz(number: int, mod1: int, mod2: int) -> str:
    result = ""
    if number % mod1 == 0:
        result += "unga"
    if number % mod2 == 0:
        result += "bunga"
    return result
