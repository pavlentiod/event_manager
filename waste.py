import pandas as pd
import math
import random

def mul_on_2d3(n: int):
    n = 0b0000000 + bin((n * 171))
    a = f'{str(n)[2:7]},{str(n)[7:9]}'
    print(a)


def complex_abs_original(z):
    # Original formula
    return math.sqrt(z.real ** 2 + z.imag ** 2)


def complex_abs_approx(z):
    # Approximation method
    a = max(abs(z.real), abs(z.imag))
    b = min(abs(z.real), abs(z.imag))
    return 0.875 * a + 0.5 * b

l = []
# Example usage:
for i in range(100):
    complex_x = random.randint(0,10)
    complex_y = random.randint(0,10)
    complex_num = complex(complex_x,complex_y)
    abs_original = complex_abs_original(complex_num)
    abs_approx = complex_abs_approx(complex_num)
    # print(f"Original formula: {abs_original}")
    # print(f"Approximation method: {abs_approx}")
    l.append(abs_original - abs_approx)

print(max(l))
