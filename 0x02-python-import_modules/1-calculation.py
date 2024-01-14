#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5

add_result = calc.add(a, b)
sub_result = calc.sub(a, b)
mul_result = calc.mul(a, b)
div_result = calc.div(a, b)

print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {sub_result}")
print(f"{a} * {b} = {mul_result}")
print(f"{a} / {b} = {div_result}")

