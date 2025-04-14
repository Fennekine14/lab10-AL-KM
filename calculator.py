# Repository Link: https://github.com/Fennekine14/lab10-AL-KM.git
# Partner 1: Alejandro Leyva
# Partner 2: Keon K. Moghaddam

import math

def add(a, b): 
    return a+b

def subtract(a, b):
    return a - b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError("Division by Zero")
    return a/b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError('Logarithm cannot be negative and must be greater than 1')
    if b <= 0:
        raise ValueError('b must be greater than 0')
    return math.log(b, a)

def exp(a,b):
    return math.pow(a,b)

def square_root(a):
    if a < 0:
        raise ValueError('A must be greater than 0')
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)