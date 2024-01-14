#!/usr/bin/python3

def add(a, b):
    """Return the sum of two integers."""
    return a + b

def sub(a, b):
    """Return the result of subtracting b from a."""
    return a - b

def mul(a, b):
    """Return the product of two integers."""
    return a * b

def div(a, b):
    """Return the result of dividing a by b as an integer."""
    return int(a / b)

if __name__ == "__main__":
    # Example usage:
    x = 10
    y = 5

    result_add = add(x, y)
    result_sub = sub(x, y)
    result_mul = mul(x, y)
    result_div = div(x, y)

    print(f"{x} + {y} = {result_add}")
    print(f"{x} - {y} = {result_sub}")
    print(f"{x} * {y} = {result_mul}")
    print(f"{x} / {y} = {result_div}")

