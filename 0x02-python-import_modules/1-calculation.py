#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print(add_result, end=' ')
    print(sub_result, end=' ')
    print(mul_result, end=' ')
    print(div_result)
