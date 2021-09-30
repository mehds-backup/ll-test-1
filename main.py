# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fizzbuzz(number: int, n1: int, n2: int) -> str:
    larger = max(n1, n2)
    smaller = min(n1, n2)

    result = ""
    if larger % smaller == 0:
        if number % larger == 0:
            return "ungabunga"
        elif number % smaller == 0:
            return "unga"

    if number % smaller == 0:
        result += "unga"
    if number % larger == 0:
        result += "bunga"
    return result


if __name__ == "__main__":
    print(fizzbuzz(15, 5, 3))

    print(fizzbuzz(56, 14, 7))
