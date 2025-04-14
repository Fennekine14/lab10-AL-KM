"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


def square_root(a):
    try:
        if a == 0:
            raise ValueError('Square root of 0 is not defined')
        return math.sqrt(a)
    except ValueError as e:
        print(f'Error: {e}')
        return None

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError('Division by Zero')
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError('Logarithm cannot be negative and must be greater than 1')
    if b <= 0:
        raise ValueError('b must be greater than 0')
    return math.log(b, a)

def exponent(a, b):
    return math.pow(a, b)