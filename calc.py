"""Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the 
following mathematical operators: +, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it 
should return 24."""

def calc(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "/":
        return n1 / n2
    elif op == "*":
        return n1 * n2
    else:
        return "Please enter a valid operator."

print(calc(6," ", 4))
