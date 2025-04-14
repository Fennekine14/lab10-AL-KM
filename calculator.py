import math

def add(a, b): 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError("Division by Zero")
    return a/b

def log(a,b):
    if a<=0 or a==1:
        raise ValueError("Logarithm cannot be negative and must be greater than 1")
    if b<=0:
        raise ValueError("b must be greater than 0")
    return math.log(b,a)

def exp(a,b):
    return math.pow(a,b)


