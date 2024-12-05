# math_functions.py

# Power function: Raises base to the exponent power
def power(base, exponent):
    return base ** exponent

# Divide function: Divides numerator by denominator
def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator

