"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

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